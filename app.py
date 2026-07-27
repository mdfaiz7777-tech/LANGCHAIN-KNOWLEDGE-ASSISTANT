from chatbot.llm import ask_ai

print("=" * 50)
print("Enterprise AI Knowledge Assistant")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    answer = ask_ai(question)
    print(f"\nAI: {answer}")