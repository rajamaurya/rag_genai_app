from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from ollama_streaming_wrapper import OllamaStreamingLLM
#from langchain.llms import OpenAI
from langchain.llms import Ollama
from langchain.agents import tool
from agents.rag_agents import rag_retrieval_tool

# prompt = PromptTemplate(
#     input_variables=["question"],
#     template="You are a helpful assistant. Reformulate this question clearly: {question}"
# )
# llm = Ollama(model="mistral", temperature=0.0),
# chain = LLMChain(llm=llm, prompt=prompt)

@tool
def reformulate_question(question: str) -> str:
    """reformulate the user's question for better understanding"""
    print(question)
    print(f"QUESTION is::  {question}, {type(question)}")
    refined_query = f"Refined: {question}"
    print("refined_query:: ", refined_query)
    result = rag_retrieval_tool.invoke({"question": refined_query})
    print("result is :: ", result)
    return result