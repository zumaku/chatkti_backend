import os
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

load_dotenv()

persist_directory = "pkti23_db"
file_path = "docs/pedoman_penulisan_kti_2023.pdf"
model="llama-3.1-70b-versatile"

if os.path.isdir(persist_directory):
    print(f"The directory {persist_directory} exists.")
    print("No need to create embedding.")
else:
    print(f"The directory {persist_directory} does not exist.")
    print("Creating the embedding.")

    # laoding the document
    print("Loading the document.")
    loader = UnstructuredPDFLoader(file_path)
    document = loader.load()

    # split into text chunks
    print("Spliting document.")
    text_spliter = CharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=400
    )

    texts = text_spliter.split_documents(document)

    # Make the embedding
    print("Creating vectordb.")
    embeddings = HuggingFaceEmbeddings()

    vectordb = Chroma.from_documents(
        documents=texts,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    
    print("Embedding is ready.")

    print("="*10)

    # Make the retriever
    retriever = vectordb.as_retriever()

    # Make the llm model
    llm = ChatGroq(
        model=model,
        temperature=0
    )

    # Create a QA chain
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