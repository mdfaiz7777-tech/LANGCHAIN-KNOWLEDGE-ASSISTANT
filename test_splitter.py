from chatbot.document_loader import load_pdf
from chatbot.text_splitter import split_documents

docs = load_pdf("uploads/Reltio_US_KT.pdf")

chunks = split_documents(docs)

print(f"Total Pages: {len(docs)}")
print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0].page_content)

print("\nMetadata:")
print(chunks[0].metadata)