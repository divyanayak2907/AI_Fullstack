from ollama import chat
response = chat(
    model="llama3.2",
      messages=[
          {
              "role": "user",
                "content": "what is SQL"
          }
                ]
            )
print(response.message.content)