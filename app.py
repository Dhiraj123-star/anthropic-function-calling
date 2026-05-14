from chatbot.chatbot import AnthropicChatbot

bot = AnthropicChatbot()

print("Anthropic AI Assistant")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower()=="exit":
        break

    bot.chat(user_input)

    print()