import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    print("Error: ANTHROPIC_API_KEY not found in .env file")
    exit(1)

# Simple terminal chat with Claude
def chat_with_claude():
    messages = []
    print("Chat with Claude (type 'exit' to quit)")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            break
            
        messages.append({"role": "user", "content": user_input})
        
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-3-7-sonnet-20250219",
                "messages": messages,
                "max_tokens": 4000
            }
        )
        
        if response.status_code == 200:
            assistant_message = response.json()["content"][0]["text"]
            print(f"\nClaude:\n{assistant_message}")
            messages.append({"role": "assistant", "content": assistant_message})
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

if __name__ == "__main__":
    chat_with_claude()
