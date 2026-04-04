import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

llm_model = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=api_key
)


def get_context(documents):
    return "\n\n".join([doc.page_content for doc in documents])


prompt_template = """
Use the context to answer the question.
If answer is not in the context, say "I don't know".

Question: {question}
Context: {context}
Answer:
"""


def answer_query(documents, query):
    context = get_context(documents)

    prompt = ChatPromptTemplate.from_template(prompt_template)
    chain = prompt | llm_model

    response = chain.invoke({
        "question": query,
        "context": context
    })

    return response.content