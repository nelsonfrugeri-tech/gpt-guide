import openai
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
        "max_tokens": int(input("Enter the max tokens: ") or 50),
        "temperature": int(input("Enter the creativity value of the text, from 0 to 1, 0 for least creative and 1 for most creative: ") or 0.5),
        "top_p": int(input("Enter the imagination value of the text, from 0 to 1, 0 for least imaginative and 1 for most imaginative: ") or 1),
        "n": int(input("How many answers would you like to receive?: ") or 1),
        "stop": input("If you want to stop the answer at any point include the text here?: ") or "",
        "best_of": input("Among the answers, if there are more than one, how many better answers do you want?: ") or 1,
        "suffix": input("Add words or text to add more context to your prompt: ") or "",
        "echo": input("Do you want to return the prompt entry in the answer?: ") or True
    }

def main():
    print(generate_completion(prompt()))

if __name__ == "__main__":
    main()
