def get_reply(user_input):
    user_input = user_input.lower()

    if user_input == "hi" or user_input == "hello":
        return "Hello! Nice to meet you 😊"
    elif user_input == "how are you":
        return "I am fine, thank you! How about you?"
    elif user_input == "what is your name":
        return "My name is ChatBot 😄"
    elif user_input == "bye":
        return "Goodbye! Have a nice day 👋"
    else:
        return "Sorry, I don't understand that."

def chatbot():
    print("🤖 ChatBot Started! (type 'bye' to exit)")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("Bot:", reply)

        if user_input.lower() == "bye":
            break

# Run chatbot
chatbot()