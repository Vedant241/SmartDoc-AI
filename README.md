# 📄 SmartDoc AI — Document Q&A Assistant

An AI-powered document question-answering system built with **RAG (Retrieval-Augmented Generation)**. Upload any PDF or text file and ask questions — get accurate answers based on the document content.

## How It Works

```
Upload Document → Split into Chunks → Generate Embeddings → Store in Vector DB
                                                                    ↓
User Asks Question → Find Relevant Chunks → Send to Gemini AI → Get Answer
```

1. **Document Loading** — Reads PDF/text files using LangChain document loaders
2. **Text Splitting** — Breaks the document into 1000-character chunks with 200-character overlap to maintain context
3. **Embedding Generation** — Converts text chunks into numerical vectors using Google's embedding model
4. **Vector Storage** — Stores embeddings in ChromaDB for fast similarity search
5. **Question Answering** — When you ask a question, it finds the 3 most relevant chunks and sends them to Gemini AI to generate an answer

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.10+** | Core language |
| **Google Gemini API** | LLM for generating answers |
| **LangChain** | RAG pipeline orchestration |
| **ChromaDB** | Vector database for storing embeddings |
| **Streamlit** | Web UI |
| **PyPDF** | PDF parsing |

## Setup & Run

**1. Clone the repository**
```bash
git clone https://github.com/VedantKundalworksiya/smartdoc-ai.git
cd smartdoc-ai
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Get a free Gemini API key**
- Go to https://aistudio.google.com/apikey
- Create a new API key
- Paste it in the `.env` file:
```
GOOGLE_API_KEY=your_key_here
```

**4. Run the application**
```bash
streamlit run app.py
```

**5. Open in browser**
- Go to `http://localhost:8501`
- Upload a PDF or text file
- Ask questions about it

## Project Structure

```
smartdoc-ai/
├── app.py              # Streamlit web interface
├── rag.py              # RAG pipeline (loading, chunking, embedding, QA)
├── requirements.txt    # Python dependencies
├── .env                # API key (not tracked in git)
└── .gitignore
```

## What is RAG?

**Retrieval-Augmented Generation (RAG)** solves a key problem with LLMs — they don't know about YOUR data. Instead of sending an entire document to the AI (which is expensive and limited by context windows), RAG:

1. Splits the document into small chunks
2. Converts chunks into embeddings (numerical vectors)
3. When you ask a question, finds only the most relevant chunks
4. Sends those chunks + your question to the LLM

This is **cheaper**, **faster**, and works with **documents of any size**.
