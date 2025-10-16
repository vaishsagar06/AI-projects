import os, json
from dotenv import load_dotenv
from openai import OpenAI
import numpy as np

load_dotenv()  
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

query = "What can't i move backwards in?"

EMBEDDING_MODEL = "text-embedding-3-small"


with open("notes.json", "r", encoding="utf-8") as f:
    notes = json.load(f)

resp = client.embeddings.create(
    input=notes,
    model=EMBEDDING_MODEL,
)

embs = [np.array(e.embedding) for e in resp.data]


q_resp = client.embeddings.create(
    input=[query],
    model=EMBEDDING_MODEL,
)
q = np.array(q_resp.data[0].embedding)

sims = [np.dot(q, e) / (np.linalg.norm(e) * np.linalg.norm(q)) for e in embs]

ranked = sorted(zip(notes, sims), key=lambda x: x[1], reverse=True)

TOP_K = 2

context = "\n\n---\n\n".join([note for note, _ in ranked[:TOP_K]] )
prompt = f"""Answer the question using ONLY the context below.
If the answer isn't in the context, say 'I don't have that in your notes yet.'

Context:
{context}

Question:
{query}
"""

resp = client.chat.completions.create(
    model="gpt-4.1-nano",
    temperature=0.2,
    messages=[
        {"role": "system", "content": "You answer strictly from the provided context."},
        {"role": "user", "content": prompt},    
    ],
)

print(resp.choices[0].message.content)
