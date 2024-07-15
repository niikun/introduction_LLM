#!/workspaces/introduction_LLM/.venv/bin/python

import os
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv(verbose=True)
client = OpenAI(api_key = os.environ["OPENAI_API_KEY"])

#generate Image

response = client.images.generate(
    model="dall-e-3",
    prompt = "A white siamese cat",
    size = "1024x1024",
    quality = "standard",
    n = 1
)

print(response.data[0].url)






##generate LLM
# response = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#         {"role":"system","content":"You are a kind woman living in Osaka Japan."},
#         {"role":"user","content":"Please tell me a soul food of Osaka.Speaking in a 'Osaka Language'."}
#     ]
# )

# print(response.choices[0].message.content)