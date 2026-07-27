import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from chatbot.config import GOOGLE_API_KEY, CHAT_MODEL

from chatbot.memory import chat_history

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

def ask_ai(question: str) -> str:
    chat_history.add_message(HumanMessage(content=question))

    response = llm.invoke(chat_history.messages)

    chat_history.add_message(AIMessage(content=response.content))

    return response.content