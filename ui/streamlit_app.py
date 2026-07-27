import os
import streamlit as st
import uuid

from chatbot.document_loader import load_pdf
from chatbot.text_splitter import split_documents
from chatbot.vector_store import create_vector_store
from chatbot.rag_chain import ask_rag

st.set_page_config(
    page_title="Faiz AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 Faiz AI Knowledge Assistant")
st.caption("Powered by LangChain + Gemini + ChromaDB")

with st.sidebar:

    st.header("📄 Document")

    st.write("Upload a PDF to create your AI knowledge base.")

    uploaded_files = st.file_uploader(
        "Upload PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        st.success(f"{len(uploaded_files)} document(s) uploaded")

        for pdf in uploaded_files:
            st.write(f"📄 {pdf.name}")

    st.divider()

    if st.button("🗑 Clear Chat"):

        st.session_state.messages.clear()

        st.rerun()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Session state
if "db_created" not in st.session_state:
    st.session_state.db_created = False

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

# Build database when uploaded files change
if uploaded_files:

    current_files = sorted([pdf.name for pdf in uploaded_files])

    if current_files != st.session_state.uploaded_files:

        all_docs = []

        with st.spinner("Creating knowledge base..."):

            for pdf in uploaded_files:

                unique_filename = f"{uuid.uuid4()}_{pdf.name}"

                file_path = os.path.join(
                    UPLOAD_FOLDER,
                    unique_filename
                )

                with open(file_path, "wb") as f:
                    f.write(pdf.getbuffer())

                docs = load_pdf(file_path)

                all_docs.extend(docs)

            chunks = split_documents(all_docs)

            create_vector_store(chunks)

        st.session_state.db_created = True

        st.session_state.uploaded_files = current_files

        st.session_state.messages = []

        st.success("Knowledge base created successfully!")

# Display previous chat messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat section
question = st.chat_input("Ask a question")

if question:

    if not st.session_state.db_created:
        st.error("Please upload a PDF first.")

    else:

        # Save user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        # Get AI response
        with st.spinner("Thinking..."):
            answer, docs = ask_rag(question)

        # Save assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

            st.markdown("---")
            st.caption("📚 Sources")

            pages = sorted(
                {
                    doc.metadata.get("page", 0) + 1
                    for doc in docs
                }
            )

            st.write(
                ", ".join(f"Page {page}" for page in pages)
            )