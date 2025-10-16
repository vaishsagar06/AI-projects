from pathlib import Path
 
NOTES_DIR = Path(__file__).resolve().parent

def load_notes():
    notes = []
    for path in NOTES_DIR.glob("*.*"):
        if path.suffix.lower() not in [".txt", ".md"]:
            continue
        text = path.read_text(encoding="utf-8")
        notes.append({"path": str(path), "text": text})
    return notes

if __name__ == "__main__":
    data = load_notes()
    print(f"✅ loaded {len(data)} notes")
    for n in data:
        print("----", n["path"])
        print(n["text"][:100])
