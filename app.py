import streamlit as st
from rag_pipeline import answer_query
from vector_database import create_db_from_uploaded_file

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown("## 🤖 DocumentBot - Ask Anything from Your Documents")

uploaded_file = st.file_uploader("📄 Upload PDF", type="pdf")

user_query = st.text_area(
    "💬 Ask something:",
    height=120,
    placeholder="Ask about your document..."
)

ask_question = st.button("🚀 Ask Question")

st.markdown('</div>', unsafe_allow_html=True)

if ask_question:

    if uploaded_file is None:
        st.error("Please upload a file first!")

    elif not user_query.strip():
        st.warning("Please enter a question!")

    else:

        db = create_db_from_uploaded_file(uploaded_file)
        
        retrieved_docs = db.similarity_search(user_query, k=3)

        response = answer_query(
            documents=retrieved_docs,
            query=user_query
        )

        if hasattr(response, "content"):
            final_answer = response.content
        else:
            final_answer = response

        st.markdown(f"""
        <div class="message">
            <div class="avatar user-avatar">🧑</div>
            <div class="bubble user">{user_query}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="message">
            <div class="avatar bot-avatar">🤖</div>
            <div class="bubble bot">{final_answer}</div>
        </div>
        """, unsafe_allow_html=True)