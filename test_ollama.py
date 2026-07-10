from ollama import chat

response = chat(
    model="mistral:latest",
    messages=[
        {
            "role": "user",
            "content": "Say Hello"
        }
    ],
)

print(response["message"]["content"])