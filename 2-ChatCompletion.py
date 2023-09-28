import os
import openai
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_KEY')

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a piece of code, and your task is to explain it in a concise way."
    },
    {
      "role": "user",
      "content": "def add(a, b): return a + b "

    }
  ],
  temperature=0,
  max_tokens=1024,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message.content.strip())
