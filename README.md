# DocumentBot – AI-Powered Document Q&A Assistant

**Live Demo:**
https://documentbot-dhukxbadfcdxjpusfy2dc6.streamlit.app/

---

## Overview

DocumentBot is an AI-based chatbot that allows users to upload documents and ask questions based on their content. It uses a Retrieval-Augmented Generation (RAG) approach to provide accurate and context-aware answers instead of generic responses.

---

## Features

* Upload and process documents
* Semantic search using vector database (FAISS)
* AI-generated answers using Groq (LLaMA 3.1)
* Simple and interactive UI built with Streamlit
* Context-aware responses based on document content

---

## Tech Stack

* Frontend: Streamlit
* Backend: Python
* LLM: Groq (LLaMA 3.1)
* Vector Database: FAISS
* Embeddings: Sentence Transformers
* Framework: LangChain

---

## Project Structure

```
DocumentBot/
│
├── app.py                  # Main Streamlit app
├── rag_pipeline.py         # RAG pipeline (retrieval + generation)
├── vector_database.py      # FAISS vector database logic
├── styles.css              # UI styling
│
├── vectorstore/
│   └── db_faiss/           # Stored embeddings
│
├── .gitignore
├── requirements.txt / Pipfile
└── README.md
```

---

## Setup Instructions (Local)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/DocumentBot.git
cd DocumentBot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set environment variable

```bash
# Windows
set GROQ_API_KEY=your_api_key_here

# Linux/Mac
export GROQ_API_KEY=your_api_key_here
```

### 4. Run the application

```bash
streamlit run app.py
```

---

## Deployment (Streamlit Cloud)

1. Push your code to GitHub
2. Go to Streamlit Community Cloud
3. Select your repository and branch
4. Set secrets in Streamlit:

```toml
GROQ_API_KEY = "your_api_key_here"
```

5. Deploy the app

---

## Security Notes

* Do not commit `.env` files
* Do not hardcode API keys in the code
* Always use environment variables or secrets

---

## Future Improvements

* Support for multiple documents
* Chat history and memory
* Highlighting answers inside documents
* Authentication system
* Improved UI/UX

---

## Author

Mayank Raj
Co-founder @ Adaciral
B.Tech Student | AI/ML Enthusiast

---

## License

This project is open-source and available under the MIT License.
