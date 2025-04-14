from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
from ollama_streaming_wrapper import OllamaStreamingLLM
#from langchain.llms import OpenAI
from langchain.llms import Ollama
# retrieve_rag_chain
def get_rag_chain():
    db = FAISS.load_local("faiss_index", HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"), allow_dangerous_deserialization=True) # vector store
    retriever = db.as_retriever(search_type="similarity", k= 3)
    chain = ConversationalRetrievalChain.from_llm(
        llm = Ollama(model="mistral", temperature=0.0),
        retriever = retriever,
        return_source_documents=True  # optional
    )
    return chain
 # get answers in stream

def get_answers_stream(response):
    # get rag chain
    # chain = get_rag_chain()
    # print("Calling chain with:")
    # print(f"question: {query}")
    # print("chat_history: []")
    # response = chain.stream({"question": query, "chat_history": []})
    # print("RESPONSE :::: ", response)
    for chunk in response:
        ans = chunk['answer']
        if "source_documents" in chunk:
            sources = "\n\nSources:\n" + "\n".join([d.metadata.get("source", "Unknown") for d in chunk["source_documents"]])
            ans += sources
        yield ans