from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI
# retrieve_rag_chain
def get_rag_chain():
    db = FAISS.load_local("faiss_index", OpenAIEmbeddings())
    retriever = db.as_retriever(search_type="similarity", k= 3)
    chain = ConversationalRetrievalChain.from_llm(
        llm = OpenAI(temarature=0, streaming=True),
        retriever = retriever
    )
    return chain
 # get answers in stream
def get_answers_stream(query):
    # get rag chain
    chain = get_rag_chain()
    response = chain.stream({"question": query})
    for chunk in response:
        ans = chunk['answer']
        if "source_documents" in chunk:
            sources = "\n\nSources:\n" + "\n".join([d.metadata.get("source", "Unknown") for d in chunk["source_documents"]])
            ans += sources
        yield ans