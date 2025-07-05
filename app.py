from flask import Flask, render_template, request
from scraper.web_scraper import scrape_url
from rag.chunker import chunk_text
from rag.embedder import create_vector_store
from rag.retriever import search_index
from rag.generator import generate_answer

app = Flask(__name__)

# Temporary memory for storing embeddings and chunks
global_index = None
global_chunks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ""
    if request.method == 'POST':
        url = request.form.get('url')
        question = request.form.get('question')

        if url and question:
            # Step 1: Scrape
            raw_text = scrape_url(url)

            # Step 2: Chunk
            chunks = chunk_text(raw_text)

            # Step 3: Embed & Create FAISS index
            index, chunks = create_vector_store(chunks)

            # Store globally for reuse (for simplicity)
            global global_index, global_chunks
            global_index = index
            global_chunks = chunks

            # Step 4: Retrieve relevant chunks
            context_chunks = search_index(question, index, chunks)

            # Step 5: Generate answer
            context = " ".join(context_chunks)
            answer = generate_answer(context, question)

    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
