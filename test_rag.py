from chatbot.retriever import retrieve_documents
from chatbot.rag_chain import ask_rag

print("=" * 60)
print("Faiz AI Knowledge Assistant")
print("Type 'exit' to quit.")
print("=" * 60)

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("\nThank you for using the Faiz AI Knowledge Assistant. Goodbye! 👋")
        break

    docs = retrieve_documents(question)

    print("\nRetrieved Chunks:\n")

    for i, doc in enumerate(docs, start=1):
        print("=" * 60)
        print(f"Chunk {i} (Page: {doc.metadata.get('page', 'N/A') + 1})")
        print("=" * 60)
        print(doc.page_content[:300])
        print()

    print("\nAI:")
    print(ask_rag(question))