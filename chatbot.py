# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey", "hii"]:
        return "Hello! How can I help you?"

    # How are you
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    # Name
    elif "your name" in user_input or "who are you" in user_input:
        return "I am a Simple Rule-Based Chatbot."

    # Help
    elif "help" in user_input:
        return "Sure! You can ask me about my name, greetings, or say bye."

    # Thank you
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome!"

    # Bye
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a nice day!"

    # Quit
    elif user_input == "quit":
        return "EXIT"

    # Unknown question
    else:
        return "Sorry, I don't understand that. Please try another question."


print("================================")
print("       SIMPLE CHATBOT")
print("================================")
print("Type 'quit' to exit the chatbot.")
print()

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)

    if response == "EXIT":
        print("Bot: Goodbye! Thanks for chatting.")
        break

    print("Bot:", response)