import os
import openai
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_KEY')

# Define the prompt and other parameters
prompt = "Fix the grammer in this text How hyou doing yesterday"
engine = "gpt-3.5-turbo-instruct"

# Make API call to OpenAI GPT-3
response = openai.Completion.create(
  engine=engine,
  prompt=prompt,
  temperature=0.6,
  max_tokens=100
)

# play with the temperature, prompts and max_tokens parameters to get different results

# Extract and print the generated response
generated_text = response.choices[0].text.strip()

print(generated_text)
