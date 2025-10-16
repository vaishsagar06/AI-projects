import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

emb = client.embeddings.create(
    input="Your text string goes here",
    model="text-embedding-3-small").data[0].embedding
print("embedding length:", len(emb))

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "You are a test assistant"},
        {"role": "user", "content": "Reply with the word pong"}
    ],
    temperature=0)
try:
    # Newer SDKs return message in choices[0].message or choices[0].delta for streaming
    msg = resp.choices[0].message
except Exception:
    # Fallback to printing full response for debugging
    print("Full response:", resp)
else:
    print(msg)
