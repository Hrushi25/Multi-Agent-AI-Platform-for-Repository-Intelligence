import { useState } from "react";

const API_BASE = "http://127.0.0.1:8000";

function App() {
  const [file, setFile] = useState(null);
  const [githubUrl, setGithubUrl] = useState("");
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);


  async function uploadFile() {
    if (!file) return alert("Select a file first");

    const formData = new FormData();
    formData.append("file", file);

    await fetch(`${API_BASE}/upload`, {
      method: "POST",
      body: formData,
    });

    alert("File uploaded successfully");
  }

  async function askQuestion() {
    if (!input) return;
  
    const userMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);
  
    const res = await fetch(`${API_BASE}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message: userMessage.content,
        github_url: githubUrl || null,
      }),
    });
  
    const data = await res.json();
  
    const aiMessage = { role: "assistant", content: data.answer };
    setMessages((prev) => [...prev, aiMessage]);
    setLoading(false);
  }
  

  return (
    <div className="app">
      <header className="header">CodeChat Lite</header>
  
      <div className="controls">
        <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        <button onClick={uploadFile}>Upload</button>
  
        <input
          placeholder="GitHub repo (optional)"
          value={githubUrl}
          onChange={(e) => setGithubUrl(e.target.value)}
        />
      </div>
  
      <div className="chat">
        {messages.map((msg, i) => (
          <div key={i} className={`bubble ${msg.role}`}>
            {msg.content}
          </div>
        ))}
  
        {loading && <div className="bubble assistant">Thinking…</div>}
      </div>
  
      <div className="inputBar">
        <textarea
          placeholder="Ask a question…"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && !e.shiftKey && askQuestion()}
        />
        <button onClick={askQuestion}>Send</button>
      </div>
    </div>
  );
  
}

export default App;
