import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def build_prompt(context, question):
    return f"""
You are an expert resume reviewer.

Resume Content:
{context}

Question:
{question}

Give a clear, professional analysis.
"""


def call_llm(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content