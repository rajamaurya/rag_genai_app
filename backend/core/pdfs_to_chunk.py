from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
def pdfs_to_chunk(filePath):
    print("FILE_PATH in pdf fn:: ", filePath)
    loader = PyPDFLoader(filePath)
    #load the docs
    documents = loader.load()
    print("Documents are::: ", documents)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents) # pass the docs to split it in chucks
    return chunks
