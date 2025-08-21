import re
def chunk_text(text: str, chunk_size: int = 800, overlap: int = 100):
    text = re.sub(r'\s+', ' ', text).strip()
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

if __name__ == "__main__":
    sample_text = """The Constitution of India is the supreme law of India.
    It lays down the framework defining fundamental political principles,
    establishes the structure, procedures, powers, and duties of government institutions,
    and sets out fundamental rights, directive principles, and the duties of citizens."""
    chunks = chunk_text(sample_text, chunk_size=50, overlap=10)
    for i, ch in enumerate(chunks, 1):
        print(f"Chunk {i}: {ch}")
