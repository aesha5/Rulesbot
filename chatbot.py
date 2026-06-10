responses = {
    "hello" : "Hello, nice to meet you!",
    "hi" : "Hi, how can I help you today?",
    "hey" : "Hey, What's up?",

    "what is you name" : "My name is Rulesbot!",
    "who created you" : "A student created me.",
    "what can you do" : "I can answer to predefined questions.",
    "how are you" : "I am Great! What about you?",
    "what are doing" : "I am a chatbot, and I am chatting with you.",

    "help" : (
        "This is how I can help you :\n"
        "I can tell you a joke.\n"
        "I can tell you today's date.\n"
        "I can tell you what year it is.\n"
        "I can tell you what language I have been coded in.\n"
    ),

    "tell me a joke" : "People say 'Bill, are you an optimist?' And I say, I hope so.",
    "what is today's date" : "7th June.",
    "what is the year" : "its 2026!",
    "what language are you coded in" : "I was coded in Python!"
}

print("===You are chatting with a rule based chatbot, Rulesbot===\n")
print("Type 'bye' or 'exit' or 'end' to end the converstaion\n")

while True:
    user=input("You: ").lower().strip()

    if user=="bye" or user=="exit" or user=="end":
        print("Bot: Goodbye, Have a nice day!")
        break
    
    print("Bot: ", responses.get(user, "Sorry, thats not a predifined question."), "\n")   
