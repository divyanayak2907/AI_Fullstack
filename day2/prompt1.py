from ollama import chat
response = chat(
    model="llama3.2",
      messages=[
          {
              "role": "user",
                "content": "explain fashion designing to beginners using headings aand bullet points  and Avoid complex fashion terminology.  Include only the basic concepts and important points.  "
          }
                ]
            )
print(response.message.content)