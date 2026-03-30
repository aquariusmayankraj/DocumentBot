from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import tempfile
import os

OLLAMA_MODEL = "deepseek-r1:1.5b"


def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    return loader.load()


def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    return text_splitter.split_documents(documents)


def get_embedding_model():
    return OllamaEmbeddings(model=OLLAMA_MODEL)



def create_db_from_uploaded_file(uploaded_file):
    """
    Creates FAISS DB from uploaded PDF (dynamic)
    """
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    try:
        documents = load_pdf(temp_path)

        chunks = create_chunks(documents)

        db = FAISS.from_documents(chunks, get_embedding_model())

        return db

    finally:

        os.remove(temp_path)