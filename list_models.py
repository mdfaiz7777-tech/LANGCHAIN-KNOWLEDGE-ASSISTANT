import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

print("Available embedding models:\n")

for model in client.models.list():
    # Print only models that support embeddings
    if "embed" in model.name.lower():
        print(model.name)