from app.utils import split_text_into_chunks

def chunk_text(text: str, max_tokens: int = 3000):
    """Split transcript into chunks to fit summarizer context."""
    return split_text_into_chunks(text, max_tokens)
