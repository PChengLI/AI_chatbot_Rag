# 🚀 Enterprise RAG Chatbot

🔥 A production-ready Retrieval-Augmented Generation (RAG) system with Hybrid Search, Reranking, and ChatGPT-style UI.

---

## ✨ Overview

📚 Full-stack AI chatbot for knowledge-based question answering over custom documents.

It combines:

- 🔍 Hybrid Retrieval (Vector + BM25)
- ⚡ BGE Reranking
- 🧠 LLM Generation
- 💾 Conversation Memory
- 🗂 Knowledge Base Management
- 💬 ChatGPT-style UI

---

## 🧠 Key Features

### 🔍 Retrieval System

- 🧊 Vector Search (Milvus)
- 🔤 BM25 Search
- 🔗 Hybrid Fusion
- 🧮 Reciprocal Rank Fusion (RRF)
- 🎯 BGE Reranker

---

### 📚 Knowledge Base

- 📤 Document upload via web UI
- 🗂 Multi-knowledge-base support
- ✂️ Chunking pipeline
- 🧬 Embedding generation
- 💾 PostgreSQL storage

---

### 💬 Chat System

- 🧠 Multi-turn conversation memory
- 🔄 Context-aware responses
- ⚙️ RAG / Chat routing
- 📌 Source tracking

---

### 🎨 Frontend

- 💬 ChatGPT-style UI
- 📎 Upload sidebar
- 🧭 Message bubbles
- ⚡ Real-time chat

---

## 🏗 System Architecture

User Query  
↓  
Hybrid Retrieval  
- Milvus Vector Search  
- BM25 Search  
- RRF Fusion  
↓  
BGE Reranker  
↓  
Context Builder  
↓  
LLM Generation  
↓  
Final Answer  

---

## 🛠 Tech Stack

### Backend

- FastAPI  
- LangChain (light usage)  
- PostgreSQL  
- SQLAlchemy  

### Retrieval

- Milvus  
- BM25  
- Hybrid Search  
- RRF Fusion  

### Embedding / Rerank

- BGE Embedding  
- BGE Reranker  
- SentenceTransformers  

## 🚀 Quick Start

### Backend

1. Create virtual environment:
   python -m venv .venv

2. Activate environment:
   source .venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run server:
   uvicorn app.main:app --reload

Backend will run at:
http://localhost:8000

---

### Frontend

1. Enter frontend directory:
   cd frontend

2. Install dependencies:
   npm install

3. Start development server:
   npm run dev

Frontend will run at:
http://localhost:5173

---

## 📌 Status

✔ Hybrid Retrieval  
✔ RRF Fusion  
✔ BGE Reranker  
✔ Conversation Memory  
✔ Knowledge Upload  
✔ Chat UI  

---

## 💡 Why this project?

- LLM System Design  
- RAG Architecture  
- Full-stack AI Engineering  
- Production-level Retrieval System  

---

## ⭐ Support

If you like this project, please give it a star ⭐
