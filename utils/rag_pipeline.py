import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# for m in client.models.list():
#     print(m.id)

def generate_answer(context, query):
    prompt = f"""You are an assistant that answers based only on the context.
    Context: {context}
    Question: {query}
    Answer:"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()