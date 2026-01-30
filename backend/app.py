from fastapi import FastAPI, UploadFile

from backend.ingestion import extract_text_from_pdf, clean_text, chunk_text
from backend.utils import create_embeddings, store_embeddings
from backend.retrieval import embed_query, retrieve_chunks
from backend.llm import build_prompt, call_llm

app = FastAPI()


@app.post("/analyze")
async def analyze_resume(file: UploadFile, query: str):
    import os
    import shutil

    UPLOAD_DIR = "data/resumes"
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file_path)
    text = clean_text(text)
    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)
    index = store_embeddings(embeddings)

    query_embedding = embed_query(query)
    relevant_chunks = retrieve_chunks(index, query_embedding, chunks)

    return {
        "message": "Resume processed successfully",
        "sample_retrieved_chunks": relevant_chunks[:2]
    }