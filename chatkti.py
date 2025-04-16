import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

load_dotenv()

class ChatKTI:
    def __init__(self):
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
        llm = ChatGroq(model="llama-3.3-70b-versatile")

        # Create a chain
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True
        )

    def get_response(self, query):
        return self.qa_chain.invoke({"query": query})
