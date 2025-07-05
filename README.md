# RAG Chatbot from URL 🚀

A beginner-friendly chatbot using Retrieval-Augmented Generation (RAG) powered by Hugging Face Transformers. You provide a URL, it scrapes the text, embeds it, stores it, and answers questions based on that content.

## Features
- URL content scraping
- Sentence embedding with Hugging Face Transformers
- Local vector database for retrieval
- Simple Flask API chatbot interface

## Requirements
- Python 3.8+
- Flask
- Transformers (Hugging Face)
- SentenceTransformers or similar
- FAISS or similar vector store
- BeautifulSoup4 / requests (for scraping)

## Setup

```bash
git clone https://github.com/yourusername/rag-chatbot-from-url.git
cd rag-chatbot-from-url
pip install -r requirements.txt
