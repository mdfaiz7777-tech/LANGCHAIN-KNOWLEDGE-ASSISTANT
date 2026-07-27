from chatbot.document_loader import load_pdf

docs = load_pdf("uploads/Reltio_US_KT.pdf")

print(f"Pages loaded: {len(docs)}")
print("-" * 50)
print(docs[0].page_content[:500])