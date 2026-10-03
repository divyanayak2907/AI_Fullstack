from ollama import chat
print("       🎊welcome to the chatbot eclipse🤖")
system_message=" you are an rapper and answer me in a rap style in 4 line rhyme and also give me a emoji at the end of your answer."
while True:
    question=input("divya👸: ")
    if question==" ":
        print("eclipse🤖:Please enter a valid question or type 'exit' to quit.")
    if question.lower().strip()=="exit":
        print("eclipse🤖:Goodbye Divya. come back soon☺️(❁´◡`❁)🤗 !")
        break
    try:

        response = chat(model="llama3.2",
      messages=[
          {
                "role": "system",
                "content": system_message
          },
          {
              "role": "user",
                "content": question
          }])
        print(f"eclipse🤖:{response.message.content}")
    except Exception as e:
        print(f"eclipse🤖: Sorry, I encountered an error: {e}")
        