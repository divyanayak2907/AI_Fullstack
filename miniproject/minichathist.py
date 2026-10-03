from ollama import chat
print("       🎊welcome to the chatbot eclipse🤖")
system_message=" you are an rapper and answer me in a rap style in 1 line rhyme and also give me a emoji at the end of your answer."
history=[{"role":"system","content":system_message}]
while True:
    question=input("divya👸: ")
    if question==" ":
        print("eclipse🤖:Please enter a valid question or type 'exit' to quit.")
        continue
    if question.lower().strip()=="/history":
        print("----your conversation history----")
        if len(history)<2:
            print("No conversation history available.")
        for msg in history[1:]:
            if msg["role"] == "user":
                speaker = "divya👸"
            else:
                speaker = "eclipse🤖"
            print(f"{speaker}: {msg['content']}")
        print("-------------------------------------")
        print()
        continue
    if question.lower().strip()=="/clear":
        history=[{"role":"system","content":system_message}]
        print("eclipse🤖:Conversation history cleared. start a fresh conversation!")
        print()
        continue
    if question.lower().strip()=="/help":
        print("----Available Commands----")
        print("/history - View conversation history")
        print("/clear - Clear conversation history")
        print("/help - Show this help message")
        print("/exit - Exit the chatbot")
        print("--------------------------")
        print()
        continue
    if question.lower().strip()=="exit":
        print("eclipse🤖:Goodbye Divya. come back soon☺️(❁´◡`❁)🤗 !")
        break
    history.append({"role":"user","content":question})
    try:
        response = chat(
            model="llama3.2",
      messages=history
      )
        reply=response.message.content
        history.append({"role":"assistant","content":reply})
        print(f"eclipse🤖:{reply}")
        print()
    except Exception as e:
        print(f"eclipse🤖: Sorry, I encountered an error: {e}")
    
        