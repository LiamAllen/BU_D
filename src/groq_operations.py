import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
print("Using Groq API Key:", groq_api_key)
client = Groq(api_key=groq_api_key)

def groq_query():
        prompt = input("input your prompt: ")
        model = "llama3-70b-8192"  # Specify the model you want to use
        messages = [
            {"role": "user", "content": prompt}
        ]

        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model,
        )

        print(chat_completion.choices[0].message.content)
# This function allows the user to perform a Groq query using their prompt.
# It constructs a Groq query based on the user's input and returns the response from the Groq API.