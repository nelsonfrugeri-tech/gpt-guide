import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the prompt that the model will complete
prompt = input("Enter a prompt: ")

# Define the number max of the tokens
max_tokens = int(input("Enter the max tokens: "))

# Define the model and parameters to use for the completion
engine = "text-davinci-003"

# Use the OpenAI API to generate a completion
response = openai.Completion.create(
    engine=engine,
    prompt=prompt,
    max_tokens=max_tokens
)

# Print the completion text
print(response.choices[0].text.strip())
