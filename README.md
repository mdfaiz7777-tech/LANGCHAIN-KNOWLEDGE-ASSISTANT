# 🤖 AI Knowledge Assistant

An AI-powered Knowledge Assistant built with **LangChain**, **Google Gemini**, **ChromaDB**, and **Streamlit** that allows users to upload one or multiple PDF documents and ask questions in natural language.

The assistant uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from uploaded documents before generating accurate answers using Google's Gemini model.

---

## 🚀 Features

* 📄 Upload one or multiple PDF documents
* 💬 Chat with your documents using natural language
* 🔍 Semantic search using ChromaDB
* 🧠 Google Gemini LLM integration
* 📚 Source page references for answers
* 💾 Persistent vector database
* 🗑 Clear chat functionality
* ⚡ Modern Streamlit user interface

---

## 🛠 Tech Stack

* Python
* LangChain
* Google Gemini
* ChromaDB
* Streamlit
* Google Generative AI Embeddings
* python-dotenv

---

## 📂 Project Structure

```text
LANGCHAIN-KNOWLEDGE-ASSISTANT/
│
├── chatbot/
│   ├── config.py
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── memory.py
│   ├── rag_chain.py
│   ├── retriever.py
│   ├── text_splitter.py
│   └── vector_store.py
│
├── ui/
│   └── streamlit_app.py
│
├── uploads/
├── chroma_db/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/mdfaiz7777-tech/LANGCHAIN-KNOWLEDGE-ASSISTANT.git

cd LANGCHAIN-KNOWLEDGE-ASSISTANT
```

### Create a virtual environment

```bash
python -m venv genv
```

### Activate the virtual environment

Windows

```bash
genv\Scripts\activate
```

macOS/Linux

```bash
source genv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_api_key_here
```

---

## ▶️ Run the Application

```bash
python -m streamlit run ui/streamlit_app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## 💡 How It Works

1. Upload one or more PDF documents.
2. Documents are loaded and split into smaller chunks.
3. Each chunk is converted into vector embeddings.
4. ChromaDB stores the embeddings.
5. User questions are converted into embeddings.
6. Relevant document chunks are retrieved.
7. Gemini generates answers using only the retrieved context.
8. The assistant displays the answer along with the source page numbers.

---

## 🔮 Future Enhancements

* Conversation memory
* Streaming AI responses
* Document citations with highlighted text
* Support for Word, Excel and PowerPoint files
* Authentication and user accounts
* Docker support
* Cloud deployment
* Voice input
* AI Agents
* LangGraph integration

---

## 🤝 Contributing

Contributions, ideas and suggestions are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Mohamed Faiz**

GitHub:
https://github.com/mdfaiz7777-tech

LinkedIn:
https://www.linkedin.com/in/mohamed-faiz-s-672b07157/
