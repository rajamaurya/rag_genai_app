from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

def get_vector_store():
     return FAISS.load_local("faiss_index", OpenAIEmbeddings())