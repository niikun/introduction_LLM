#!/workspaces/introduction_LLM/.venv/bin/python
import os
from dotenv import load_dotenv
# import pandas
# from qdrant_client import models, QdrantClient
# from sentence_transformers import SentenceTransformer
from openai import OpenAI

load_dotenv(verbose=True)

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining about curry & rice in Japanese."},
    {"role": "user", "content": "Compose a poem that explains the concept of spice like in Japanese like a Osaka woman."}
  ]
)

print(completion.choices[0].message.content)