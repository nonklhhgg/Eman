from nltk.chat.util import Chat, reflections
from word_utils import get_meaning, get_synonyms, get_antonyms

def main():
    print("Welcome to Word Explorer Chatbot!")
    chat_pairs = [
        # Define your chat patterns and responses here
        # Example: (r'meaning (.*)', get_meaning),
        #          (r'synonyms (.*)', get_synonyms),
        #          (r'antonyms (.*)', get_antonyms),
    ]

    chatbot = Chat(chat_pairs, reflections)
    print("Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
