from nltk.chat.util import Chat, reflections
from responses import pairs, get_meaning, get_synonyms, get_antonyms

def chat():
    # Print a welcome message
    print("Hi! I am a chatbot. How can I help you today?")
    
    # Create a Chat instance with predefined pairs and reflections
    chat_instance = Chat(pairs, reflections)

    while True:
        try:
            # Get user input
            user_input = input("> ")
            
        except KeyboardInterrupt:
            print("Goodbye!")
            break
            
        # If the user input is "quit", exit the loop
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        else:
            # Remove leading/trailing whitespace
            user_input = user_input.strip()
            
            # If the user input ends with a question mark
            if user_input.endswith("?"):
                # Get a response from the Chat instance
                response = chat_instance.respond(user_input)
            else:
                # If the user input does not end with a question mark
                # Split the input into a list of words
                words = user_input.split()
                
                # If the word "meaning" is present in the input
                if "meaning" in words:
                    word = words[-1].rstrip("s")
                    response = get_meaning(word)
                elif "synonyms" in words:
                    word = words[-1].rstrip("s")
                    response = get_synonyms(word)
                elif "antonyms" in words:
                    word = words[-1].rstrip("s")
                    response = get_antonyms(word)
                else:
                    # If none of the specific keywords are present in the input
                    # Get a general response from the Chat instance
                    response = chat_instance.respond(user_input)
            
            # Print the response
            print(response)

if __name__ == "__main__":
    # Call the chat function
    chat()
