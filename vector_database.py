from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import tempfile
import os


# 🔹 Load PDF
def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    return loader.load()


# 🔹 Split into chunks
def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    return text_splitter.split_documents(documents)


# 🔹 Embedding model (Cloud compatible)
def get_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


# 🔹 Create FAISS DB from uploaded file
def create_db_from_uploaded_file(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    try:
        # Load PDF
        documents = load_pdf(temp_path)

        # Split into chunks
        chunks = create_chunks(documents)

        # Create vector DB
        db = FAISS.from_documents(
            chunks,
            embedding=get_embedding_model()
        )

        return db

    finally:
        # Clean up temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)