from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from core.vector_store import get_vector_store
from dotenv import load_dotenv
load_dotenv()

import os

# convert chunks into vectore and store it in vectore DB FAISS
def embed_and_store(chunks):
    #if index already exist the load from local and add the new chunk and save locally
    db = None
    if os.path.exists("faiss_index"):
        db = get_vector_store()
        db.add_documents(chunks)
        db.save_local("faiss_index")
    else:
        db = FAISS.from_documents(chunks, OpenAIEmbeddings())
        db.save_local("faiss_index")


