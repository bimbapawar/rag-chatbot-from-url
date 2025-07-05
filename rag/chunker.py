def chunk_text(text, max_words=200):
    """
    Splits large text into smaller chunks for embedding and retrieval.

    Args:
        text (str): The full input text to be chunked.
        max_words (int): Maximum number of words per chunk.

    Returns:
        List[str]: List of chunked text strings.
    """
    words = text.split()
    chunks = [
        ' '.join(words[i:i + max_words])
        for i in range(0, len(words), max_words)
    ]
    return chunks
