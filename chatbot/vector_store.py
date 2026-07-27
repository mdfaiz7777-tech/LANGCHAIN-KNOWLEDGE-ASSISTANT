from langchain_chroma import Chroma

from chatbot.embeddings import get_embeddings


PERSIST_DIRECTORY = "chroma_db"


def create_vector_store(chunks):
    """
    Creates a new Chroma vector database from document chunks.
    """

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=PERSIST_DIRECTORY,
    )

    return vector_store


def load_vector_store():
    """
    Loads the existing Chroma vector database.
    """

    vector_store = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=get_embeddings(),
    )

    return vector_store