from langchain.agents import tool
from ollama_streaming_wrapper import OllamaStreamingLLM
from core.rag_chain import get_rag_chain

@tool
def rag_retrieval_tool(question: str) -> str:
    """Run a query through the RAG retrieval chain."""
    print("IN RAG RETRIEVAL AGENT TOOL")
    chain = get_rag_chain()
    output = chain.invoke({"question": question, "chat_history":[]})
    return output["answer"]