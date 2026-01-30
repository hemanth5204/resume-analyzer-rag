# resume-analyzer-rag

This project is an end-to-end **Resume Analyzer** built using the concept of **Retrieval-Augmented Generation (RAG)**.  
The system processes uploaded resumes (PDF format), extracts meaningful information, and retrieves the most relevant resume sections based on a user query using **semantic search**.

Instead of relying on keyword matching, the application uses **vector embeddings and similarity search**, making the analysis more accurate and context-aware. The backend is implemented using **FastAPI** and is designed in a modular and scalable way.

## ⚙️ System Workflow

1. User uploads a resume (PDF) through the API.
2. Resume text is extracted and cleaned.
3. The text is split into smaller overlapping chunks.
4. Each chunk is converted into vector embeddings using a Sentence Transformer model.
5. All embeddings are stored in a FAISS vector index.
6. When a user submits a query (e.g., role-based analysis), the query is embedded.
7. FAISS retrieves the most relevant resume chunks using semantic similarity.
8. The retrieved sections are returned as the analysis context.

## 🧠 Architecture Overview

Resume (PDF)
   ↓
Text Extraction & Cleaning
   ↓
Chunking
   ↓
Embedding Generation
   ↓
FAISS Vector Store
   ↓
Semantic Retrieval (RAG)
   ↓
Relevant Resume Sections

## 🖼️ Screenshots

The screenshots included in this repository demonstrate:
- FastAPI Swagger UI interface
- Resume upload functionality
- Query-based resume analysis
- Retrieved resume sections based on semantic similarity

<img width="1437" height="777" alt="Screenshot 2026-01-30 at 1 22 57 PM" src="https://github.com/user-attachments/assets/6b4186db-fa29-46e5-84d3-e5cc0c03ceb8" />

## 🛠️ Tech Stack

- Python
- FastAPI
- SentenceTransformers
- FAISS (Vector Database)
- pdfplumber
- Uvicorn
- Git & GitHub

## ⭐ Key Highlights

- Implements **Retrieval-Augmented Generation (RAG)** architecture
- Uses **semantic vector search** instead of keyword matching
- Modular backend design for easy extension
- Industry-relevant AI backend project
- Easily extendable to:
  - Job Description vs Resume matching
  - Resume scoring (ATS-style)
  - LLM-based resume analysis
 
