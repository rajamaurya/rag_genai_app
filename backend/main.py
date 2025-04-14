from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from core.pdfs_to_chunk import pdfs_to_chunk
from embeddings.embed_and_store import embed_and_store
import shutil
from typing import List
from langchain.llms import Ollama

from agents.rag_agents import rag_retrieval_tool
from agents.stream_answer import get_answers_stream
from agents.user_agent import reformulate_question
from langchain.agents import initialize_agent, AgentType


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

tools = [rag_retrieval_tool, reformulate_question, get_answers_stream]

agent = initialize_agent(
    tools= tools,
    llm = Ollama(model="mistral", temperature=0.0),
    agent =AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True
)

@app.post("/ask")
def ask(query: Query):
    reformulate_question(query.question)
    return StreamingResponse(agent.run(generateAnswerChunk(query)), media_type="text/plain")


def generateAnswerChunk(query):
    print("QUESTION IS :::::: ", query)
    for chunk in get_answers_stream(query.question):
        yield chunk



