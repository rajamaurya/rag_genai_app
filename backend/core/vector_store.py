from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

def get_vector_store():
     return FAISS.load_local(
          "faiss_index",
          HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
          allow_dangerous_deserialization=True
          )