def split_text_into_chunks(text: str, max_tokens: int = 3000):
    """Split text by approximate token count (word-based)."""

    words = text.split()
    chunks = []
    current = []

    for w in words:
        current.append(w)

        if len(current) >= max_tokens:
            chunks.append(" ".join(current))
            current = []

    if current:
        chunks.append(" ".join(current))

    return chunks
