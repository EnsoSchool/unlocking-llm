import os
import openai
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_KEY')

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a block of text, and your task is to extract a list"
                 " of keywords and its sentiment from it."
    },
    {
      "role": "user",
      "content": ""
    },
    {
      "role": "assistant"
    }
  ],
  temperature=0.5,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
print(response.choices[0].message.content.strip())
