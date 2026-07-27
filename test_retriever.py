from chatbot.retriever import retrieve_documents

question = input("Ask a question: ")

docs = retrieve_documents(question)

print("\nRetrieved Documents:\n")

for i, doc in enumerate(docs, start=1):
    print("=" * 60)
    print(f"Chunk {i}")
    print("=" * 60)
    print(doc.page_content[:500])