import sys
sys.stdout.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Придумай 3 креативных названия для моего проекта: Ассистент для оценки внедрения MDM-системы",
        }
    ],
)

print(response.choices[0].message.content)
