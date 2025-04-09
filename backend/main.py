from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from core.pdfs_to_chunk import pdfs_to_chunk
from embeddings.embed_and_store import embed_and_store
from core.rag_chain import get_answers_stream
import shutil
from typing import List

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

class Query(BaseModel):
    question:str

@app.post('/upload')
def upload_pdfs(files: List[UploadFile]=File(...)):
    print("In upload....loading files")
    for file in files:
        path = f"data/{file.filename}"
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        chunks = pdfs_to_chunk(path)
        embed_and_store(chunks)
    return "message: file uploaded scuccessfully"

@app.post("/ask")
def ask(query: Query):
    return StreamingResponse(generateAnswerChunk(query), media_type="text/plain")

def generateAnswerChunk(query):
    for chunk in get_answers_stream(query.question):
        yield chunk

