#!/workspaces/introduction_LLM/.venv/bin/python
import os
import json
from dotenv import load_dotenv
import pandas as pd
from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer
from openai import OpenAI

load_dotenv(verbose=True)

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

with open("top_rated_wines.json") as f:
    wines = json.load(f)

encoder = SentenceTransformer("all-MiniLM-L6-v2")
qdrant = QdrantClient(":memory:")
qdrant.recreate_collection(
    collection_name="top_wines",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),
        distance=models.Distance.COSINE
    )
)

qdrant.upload_points(
    collection_name="top_wines",
    points=[
        models.PointStruct(
            id=idx,
            vector=encoder.encode(doc["notes"]).tolist(),
            payload=doc
        ) for idx,doc in enumerate(wines)
    ]
)

hits = qdrant.search(
    collection_name="top_wines",
    query_vector=encoder.encode("a Malbec wine from Argentina").tolist(),
    limit=3
)
search_results = [hit.payload for hit in hits]

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining about wines in Japanese."},
    {"role": "user", "content": "Suggest me an amazing Malbec wine from Argentina.Tell me about it in Japanese."},
    {"role":"assistant","content":str(search_results)}
  ]
)

print(completion.choices[0].message.content)