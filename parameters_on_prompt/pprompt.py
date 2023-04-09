import openai
from dotenv import load_dotenv
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_completion(params):
    return openai.Completion.create(
        engine=os.getenv("OPENAI_MODEL"),
        prompt=params.get("prompt", "How can you help me?"),
        max_tokens=params.get("max_tokens", 50)
    ).choices[0].text.strip()

def prompt():
    return {
        "prompt": input("Enter a prompt: "),
        "max_tokens": int(input("Enter the max tokens: "))
    }

def main():
    print(generate_completion(prompt()))

if __name__ == "__main__":
    main()
