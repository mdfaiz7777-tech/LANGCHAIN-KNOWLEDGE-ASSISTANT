from chatbot.llm import llm
from chatbot.retriever import retrieve_documents


def ask_rag(question: str):

    docs = retrieve_documents(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
You are an AI assistant answering questions about an uploaded document.

Use ONLY the provided context.

If the answer is partially available, answer using the available information.

If the answer is not found anywhere in the context, reply exactly:

"I couldn't find this information in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content, docs