from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def review_code(diff):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "system",
                "content": "You are a strict senior code reviewer. Focus on bugs, bad practices, and improvements."
            },
            {
                "role": "user",
                "content": f"Review this code diff:\n\n{diff}"
            }
        ]
    )

    return response.choices[0].message.content