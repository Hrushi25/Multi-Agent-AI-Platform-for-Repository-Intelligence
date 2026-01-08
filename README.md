CodeChat Lite

It is a lightweight, open-source demonstration of the core architecture and agent workflows behind CodeChat, a full-scale, production-grade AI platform I built while working at DreamStudio (non-profit).

This repository intentionally focuses on a simplified subset of the system to make the design easy to understand, run locally, and discuss in interviews, while the README documents the complete capabilities of the original CodeChat platform.

🚀 The Full CodeChat Platform (DreamStudio)

While at DreamStudio, I built CodeChat, a comprehensive, enterprise-ready AI system with the following capabilities:

🧠 AI & Agent Architecture

Multi-agent architecture with specialized agents for:

Conversational chat
Document ingestion and indexing
Code understanding and execution
Diagram generation
GitHub repository analysis
Dynamic agent routing and orchestration
Tool-augmented LLM workflows
Prompt governance and agent isolation

📄 Multimodal Knowledge Ingestion

Upload and analyze:

PDFs, text files, markdown, and code files
GitHub repositories (entire repos, branches, PRs)
Chunking strategies optimized for:
Code
Documentation
Structured and unstructured text
Semantic embeddings and vector-based retrieval

🔍 Retrieval-Augmented Generation (RAG)

High-precision semantic search
Context assembly across multiple documents
Strict grounding of LLM responses in retrieved context
Hallucination-resistant answer generation
Configurable retrieval depth and relevance scoring

🧑‍💻 GitHub MCP & Developer Intelligence

GitHub repository ingestion
File-level and repo-level semantic search
Code-aware retrieval and explanation
Architecture and dependency analysis
Support for developer workflows and code navigation

🏢 Enterprise & Platform Capabilities

Authentication and role-based access control (RBAC)
Usage tracking and rate limiting
Billing and quota enforcement
Admin dashboards and analytics
Audit logging and activity tracking
Secure API key management
Environment-based configuration (dev / staging / prod)

📊 Observability & Operations

Usage metrics and analytics
Error tracking and logging
Agent-level performance monitoring
System health dashboards
Production deployment workflows

🌐 User Experience

Rich chat-based UI
Multi-session conversation history
Document and repo management
Admin interfaces for monitoring and control
Scalable, production-ready frontend architecture

🧩 What This Repository (CodeChat Lite) Demonstrates

This repository is a distilled demo that focuses on the core technical ideas behind the full platform:

📄 File upload and ingestion
🔍 Semantic embeddings using sentence-transformers
🧠 Retrieval-augmented generation (RAG)
🤖 Context-grounded answers using Gemini
🗂️ Lightweight GitHub repository ingestion (MCP-lite)
💬 ChatGPT-style UI built with React
❌ No hallucination when context is missing
