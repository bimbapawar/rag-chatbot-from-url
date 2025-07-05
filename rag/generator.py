from transformers import pipeline

# Load the Hugging Face model for question answering
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_answer(context, question):
    """
    Generates an answer based on the provided context and question using a transformer model.

    Args:
        context (str): The relevant text retrieved from the document.
        question (str): The user's question.

    Returns:
        str: The generated answer.
    """
    prompt = f"Answer the question based on the context:\nContext: {context}\nQuestion: {question}"
    result = qa_pipeline(prompt, max_length=200, do_sample=False)

    return result[0]['generated_text']
