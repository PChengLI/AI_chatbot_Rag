# 🚀 Enterprise RAG Chatbot

🔥 A production-ready Retrieval-Augmented Generation (RAG) system with Hybrid Search, Reranking, and ChatGPT-style UI.

---

## ✨ Overview

📚 This project is a full-stack AI chatbot that enables **knowledge-based question answering** over custom documents.

It combines:

- 🔍 Hybrid Retrieval (Vector + BM25)
- ⚡ BGE Reranking
- 🧠 LLM Generation
- 💾 Conversation Memory
- 🗂 Knowledge Base Management
- 💬 ChatGPT-style UI

---

## 🧠 Key Features

### 🔍 Advanced Retrieval

- 🧊 Vector Search (Milvus)
- 🔤 BM25 Sparse Retrieval
- 🔗 Hybrid Retrieval
- 🧮 Reciprocal Rank Fusion (RRF)
- 🎯 BGE Cross-Encoder Reranker

---

### 📚 Knowledge Base

- 📤 Upload documents via web UI
- 🗂 Multi-knowledge-base support
- ✂️ Text chunking pipeline
- 🧬 Embedding generation
- 💾 Persistent storage (PostgreSQL)

---

### 💬 Conversational AI

- 🧠 Multi-turn conversation memory
- 🔄 Context-aware responses
- ⚙️ RAG / Chat mode routing
- 📌 Source tracking

---

### 🎨 Frontend (ChatGPT Style)

- 💬 ChatGPT-like interface
- 📎 Knowledge base upload sidebar
- 🧭 Left/right message bubbles
- ⚡ Real-time interaction
- 🎯 Clean & minimal UI

---

## 🏗 System Architecture

```text
User Query
   ↓
🔍 Hybrid Retrieval
   ├── 🧊 Milvus Vector Search
   ├── 🔤 BM25 Search
   └── 🔗 RRF Fusion
   ↓
🎯 BGE Reranker
   ↓
📦 Context Builder
   ↓
🧠 LLM Generation
   ↓
💬 Final Answer

⚙️ How It Works
📥 Step 1: Document Ingestion
Upload file 📤
Chunk text ✂️
Generate embeddings 🧬
Store in Milvus + PostgreSQL

❓ Step 2: Query Process
User asks question 💬
Generate query embedding 🧠
Hybrid retrieval 🔍
Reranking 🎯
Build context 📦
LLM generates answer ⚡
Save conversation memory

🚀 Quick Start
📦 Clone Repository
git clone https://github.com/yourname/enterprise-rag-chatbot.git
cd enterprise-rag-chatbot
🖥 Backend Setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

📍 Backend:
http://localhost:8000

🌐 Frontend Setup
cd frontend
npm install
npm run dev

📍 Frontend:
http://localhost:5173

💡 Why This Project?

This project demonstrates:

🧠 LLM system design
🔍 Retrieval-Augmented Generation
🏗 Backend architecture design
💬 Full-stack AI engineering
⚙️ Production-level RAG pipeline
📜 License

MIT License © 2026

⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
