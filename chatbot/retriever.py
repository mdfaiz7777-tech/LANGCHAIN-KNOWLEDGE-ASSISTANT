from chatbot.vector_store import load_vector_store


def retrieve_documents(question):
    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 8}
    )

    docs = retriever.invoke(question)

    return docs