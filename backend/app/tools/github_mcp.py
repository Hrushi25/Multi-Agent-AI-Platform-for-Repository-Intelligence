import requests
from typing import List, Tuple
from app.config import settings

GITHUB_API_BASE = "https://api.github.com"

HEADERS = {
    "Accept": "application/vnd.github+json"
}

if settings.GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {settings.GITHUB_TOKEN}"


def parse_repo_url(repo_url: str) -> Tuple[str, str]:
    """
    https://github.com/owner/repo -> (owner, repo)
    """
    parts = repo_url.rstrip("/").split("/")
    return parts[-2], parts[-1]


def fetch_repo_tree(owner: str, repo: str, branch: str = "main"):
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    return resp.json()["tree"]


def fetch_file(owner: str, repo: str, path: str, branch: str = "main") -> str:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    data = resp.json()

    if data["encoding"] == "base64":
        import base64
        return base64.b64decode(data["content"]).decode("utf-8")

    return ""


def fetch_repo_files(repo_url: str, max_files: int = 20) -> List[Tuple[str, str]]:
    owner, repo = parse_repo_url(repo_url)
    tree = fetch_repo_tree(owner, repo)

    collected = []

    for item in tree:
        if item["type"] != "blob":
            continue

        path = item["path"]

        if not path.endswith((".py", ".js", ".ts", ".md")):
            continue

        if len(collected) >= max_files:
            break

        try:
            content = fetch_file(owner, repo, path)
            collected.append((path, content))
        except Exception:
            continue

    return collected
