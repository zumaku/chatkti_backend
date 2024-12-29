import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

load_dotenv()

# Make the embedding
embeddings = HuggingFaceEmbeddings()
persist_directory = "pkti23_db"

# load the chroma db
vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embeddings
)

# Retriever
retriever = vectordb.as_retriever()

# LLM
llm = ChatGroq(model="llama-3.1-70b-versatile")

# Create a chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

while(True):
    query = input("Enter your question: ")
    if query == "/exit":
        break
    response = qa_chain.invoke({"query": query})
    print("Respons:")
    print(response["result"])