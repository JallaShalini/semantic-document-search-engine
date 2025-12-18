from pathlib import Path

def load_documents(data_dir):
    data_path = Path(data_dir)
    if not data_path.exists():
        raise FileNotFoundError("Document directory not found")

    documents = []
    for file in data_path.glob("*.txt"):
        text = file.read_text(encoding="utf-8").strip()
        if text:
            documents.append({
                "id": file.stem,
                "filename": file.name,
                "text": text
            })

    if len(documents) < 100:
        raise ValueError("At least 100 documents required")

    return documents
