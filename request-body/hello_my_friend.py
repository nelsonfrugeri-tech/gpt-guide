import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the prompt that the model will complete
prompt = "Hello my friend! What's time is it?"

# Define the model and parameters to use for the completion
model_engine = "text-davinci-003"

# Use the OpenAI API to generate a completion
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
)

# Print the completion text
print(response.choices[0].text.strip())
