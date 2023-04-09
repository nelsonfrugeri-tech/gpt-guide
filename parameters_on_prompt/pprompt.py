import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set the model to use for the completion
engine = os.getenv("OPENAI_MODEL")

def generate_completion(params):

    # Use the OpenAI API to generate a completion
    response = openai.Completion.create(
        engine=engine,
        prompt=params.get("prompt", "How can you help me?"),
        max_tokens=params.get("max_tokens", 50)
    )

    return response.choices[0].text.strip()

def main():

    params = {}

    # Define the prompt that the model will complete
    params["prompt"] = input("Enter a prompt: ")

    # Define the number max of the tokens
    params["max_tokens"] = int(input("Enter the max tokens: "))

    # Print the completion text
    print(generate_completion(params))

if __name__ == "__main__":
    main()
