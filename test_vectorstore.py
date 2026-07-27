from chatbot.document_loader import load_pdf
from chatbot.text_splitter import split_documents
from chatbot.vector_store import create_vector_store

docs = load_pdf("uploads/Reltio_US_KT.pdf")
chunks = split_documents(docs)

vector_store = create_vector_store(chunks)

print(f"Documents: {len(docs)}")
print(f"Chunks: {len(chunks)}")
print("✅ ChromaDB created successfully!")