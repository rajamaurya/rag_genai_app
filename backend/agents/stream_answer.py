from langchain.agents import tool
from agents.rag_agents import rag_retrieval_tool
from core.rag_chain import get_rag_chain

@tool
def get_answers_stream(question):
    """stream answers in chunk received from rag_retrieval_tool"""
    # get rag chain
    chain = get_rag_chain()
    # print("Calling chain with:")
    print(f"question: {question}")
    # print("chat_history: []")
    response = chain.stream({"question": question, "chat_history": []})
    print("RESPONSE :::: ", response)
    for chunk in response:
        ans = chunk['answer']
        if "source_documents" in chunk:
            sources = "\n\nSources:\n" + "\n".join([d.metadata.get("source", "Unknown") for d in chunk["source_documents"]])
            ans += sources
        yield ans