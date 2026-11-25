# CodeAlpha - Basic Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hello", "hi", "hey", "hii"]:
        return "Hello! How can I help you?"

    # How are you
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    # Bot name
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm a Basic Python Chatbot created using Python."

    # Bot capabilities
    elif "what can you do" in user_input:
        return "I can answer basic questions, greetings, and some programming-related questions."

    # Creator
    elif "who created you" in user_input or "who made you" in user_input:
        return "I was created as a Python project for the CodeAlpha Internship."

    # Python
    elif "what is python" in user_input:
        return "Python is a popular programming language used for web development, automation, data science, AI, and more."

    # Java
    elif "what is java" in user_input:
        return "Java is a popular object-oriented programming language used for software, web, and application development."

    # AI
    elif "what is ai" in user_input or "what is artificial intelligence" in user_input:
        return "AI stands for Artificial Intelligence. It enables computers to perform tasks that normally require human intelligence."

    # Programming
    elif "what is programming" in user_input:
        return "Programming is the process of writing instructions that tell a computer what to do."

    # Help
    elif user_input == "help":
        return "You can ask me about Python, Java, AI, programming, my name, or what I can do."

    # Thank you
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! Happy to help."

    # Exit
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!"

    # Unknown question
    else:
        return "I'm still learning. Please try asking me something else."


print("=" * 50)
print("            BASIC PYTHON CHATBOT")
print("=" * 50)
print("Type 'bye' to exit the chatbot.")
print("You can ask about Python, Java, AI, and programming.\n")

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)
    print("Bot:", response)

    if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
        break

print("\nThank you for using the chatbot!")