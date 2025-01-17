# import nltk
# import os

# # Create a directory for NLTK data
# nltk_data_dir = 'C:\\nltk_data'
# if not os.path.exists(nltk_data_dir):
#     os.makedirs(nltk_data_dir)

# # Set the NLTK data path
# nltk.data.path.append(nltk_data_dir)

# # Download required NLTK data
# for package in ['punkt', 'averaged_perceptron_tagger', 'wordnet', 'stopwords']:
#     try:
#         nltk.download(package, download_dir=nltk_data_dir)
#         print(f"Successfully downloaded {package}")
#     except Exception as e:
#         print(f"Error downloading {package}: {e}")
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# from textblob import TextBlob
# import json
# import random
# import datetime
# # import os

# class SimpleChatbot:
#     def __init__(self):
#         # Download required NLTK data
#         try:
#             nltk.download('punkt', quiet=True)
#             nltk.download('stopwords', quiet=True)
#             nltk.download('wordnet', quiet=True)
#             nltk.download('averaged_perceptron_tagger', quiet=True)
#         except:
#             print("Note: NLTK data already downloaded or error in downloading")

#         # Initialize processing tools
#         self.lemmatizer = WordNetLemmatizer()
#         self.stop_words = set(stopwords.words('english'))
        
#         # Load responses
#         self.responses = self._load_responses()
        
#         # Initialize conversation history
#         self.conversation_history = []
        
#     def _load_responses(self):
#         """Load or create default response patterns"""
#         default_responses = {
#             'greeting': [
#                 "Hi! How can I help you today?",
#                 "Hello! What's on your mind?",
#                 "Hey there! How are you doing?",
#                 "Greetings! How may I assist you?"
#             ],
#             'how_are_you': [
#                 "I'm doing well, thank you for asking! How about you?",
#                 "I'm great! How are you today?",
#                 "All good here! How are you feeling?"
#             ],
#             'goodbye': [
#                 "Goodbye! Have a great day!",
#                 "See you later! Take care!",
#                 "Bye! It was nice chatting with you!"
#             ],
#             'thanks': [
#                 "You're welcome!",
#                 "Glad I could help!",
#                 "My pleasure!"
#             ],
#             'default': [
#                 "I'm not sure I understand. Could you rephrase that?",
#                 "Interesting! Can you tell me more?",
#                 "Could you elaborate on that?"
#             ]
#         }
        
#         # Try to load custom responses if file exists
#         try:
#             if os.path.exists('responses.json'):
#                 with open('responses.json', 'r') as f:
#                     return json.load(f)
#         except:
#             pass
            
#         return default_responses

#     def _preprocess(self, text):
#         """Preprocess the input text"""
#         # Tokenize and convert to lowercase
#         tokens = word_tokenize(text.lower())
        
#         # Remove stop words and lemmatize
#         tokens = [self.lemmatizer.lemmatize(token) for token in tokens 
#                  if token not in self.stop_words and token.isalnum()]
        
#         return tokens

#     def _analyze_intent(self, tokens):
#         """Determine the intent of the message"""
#         # Define intent patterns
#         greeting_words = {'hi', 'hello', 'hey', 'greetings'}
#         how_are_you_words = {'how', 'are', 'you'}
#         goodbye_words = {'bye', 'goodbye', 'farewell', 'cya'}
#         thanks_words = {'thanks', 'thank', 'appreciate'}
        
#         # Convert tokens to set for intersection
#         token_set = set(tokens)
        
#         # Check intents
#         if token_set.intersection(greeting_words):
#             return 'greeting'
#         elif token_set.intersection(how_are_you_words):
#             return 'how_are_you'
#         elif token_set.intersection(goodbye_words):
#             return 'goodbye'
#         elif token_set.intersection(thanks_words):
#             return 'thanks'
            
#         return 'default'

#     def respond(self, user_input):
#         """Generate a response to user input"""
#         if not user_input.strip():
#             return "I'm listening... 🌞"
            
#         # Preprocess input
#         tokens = self._preprocess(user_input)
        
#         # Analyze sentiment
#         sentiment = TextBlob(user_input).sentiment.polarity
        
#         # Determine intent
#         intent = self._analyze_intent(tokens)
        
#         # Get response based on intent
#         response = random.choice(self.responses.get(intent, self.responses['default']))
        
#         # Add to conversation history
#         self.conversation_history.append({
#             'user_input': user_input,
#             'response': response,
#             'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         })
        
#         return response

#     def save_history(self):
#         """Save conversation history to file"""
#         with open('chat_history.json', 'w') as f:
#             json.dump(self.conversation_history, f, indent=2)

# # Main chat interface
# def main():
#     # Initialize the chatbot
#     chatbot = SimpleChatbot()
    
#     print("Chatbot initialized! Type 'quit' to exit.")
#     print("-" * 50)
    
#     while True:
#         user_input = input("You: ").strip()
        
#         if user_input.lower() == 'quit':
#             print("Saving chat history...")
#             chatbot.save_history()
#             print("Goodbye!")
#             break
            
#         response = chatbot.respond(user_input)
#         print(f"Bot: {response}")

# if __name__ == "__main__":
#     main()
# # import nltk
# # nltk.download('punkt')
# # nltk.download('stopwords')
# # nltk.download('wordnet')
# # nltk.download('averaged_perceptron_tagger')

# import re
# from datetime import datetime
# from collections import deque
# import random
# import json

# class AdvancedChatbot:
#     def __init__(self, knowledge_base_file="knowledge_base.json"):
#         # Initialize conversation history
#         self.conversation_history = deque(maxlen=10)
#         # Load knowledge base
#         try:
#             with open(knowledge_base_file, 'r') as f:
#                 self.knowledge_base = json.load(f)
#         except FileNotFoundError:
#             self.knowledge_base = {
#                 "greetings": ["hello", "hi", "hey", "greetings"],
#                 "farewells": ["goodbye", "bye", "see you", "farewell"],
#                 "responses": {
#                     "greeting": ["Hello! How can I help you today?", "Hi there! What's on your mind?"],
#                     "farewell": ["Goodbye! Have a great day!", "See you later! Take care!"],
#                     "unknown": ["I'm not sure about that.", "Could you rephrase that?", "I don't understand."],
#                     "thanks": ["You're welcome!", "Happy to help!", "Anytime!"]
#                 },
#                 "patterns": {
#                     "time": r"what(?:'s|\s+is)\s+the\s+time",
#                     "thanks": r"thank(?:s|\s+you)",
#                     "weather": r"(?:what's|what\s+is)\s+the\s+weather"
#                 }
#             }
        
#     def preprocess_input(self, user_input):
#         """Clean and normalize user input"""
#         # Convert to lowercase
#         cleaned_input = user_input.lower().strip()
#         # Remove extra whitespace
#         cleaned_input = ' '.join(cleaned_input.split())
#         return cleaned_input

#     def pattern_match(self, user_input):
#         """Check if input matches any known patterns"""
#         for intent, pattern in self.knowledge_base["patterns"].items():
#             if re.search(pattern, user_input):
#                 return intent
#         return None

#     def get_response(self, user_input):
#         """Generate appropriate response based on user input"""
#         processed_input = self.preprocess_input(user_input)
        
#         # Add to conversation history
#         self.conversation_history.append(("user", processed_input))
        
#         # Check for patterns
#         pattern_match = self.pattern_match(processed_input)
#         if pattern_match:
#             response = self.handle_pattern(pattern_match)
#             self.conversation_history.append(("bot", response))
#             return response
            
#         # Check for greetings
#         if any(greeting in processed_input for greeting in self.knowledge_base["greetings"]):
#             response = random.choice(self.knowledge_base["responses"]["greeting"])
#             self.conversation_history.append(("bot", response))
#             return response
            
#         # Check for farewells
#         if any(farewell in processed_input for farewell in self.knowledge_base["farewells"]):
#             response = random.choice(self.knowledge_base["responses"]["farewell"])
#             self.conversation_history.append(("bot", response))
#             return response
            
#         # Check for thanks
#         if re.search(self.knowledge_base["patterns"]["thanks"], processed_input):
#             response = random.choice(self.knowledge_base["responses"]["thanks"])
#             self.conversation_history.append(("bot", response))
#             return response
        
#         # Default response for unknown inputs
#         response = random.choice(self.knowledge_base["responses"]["unknown"])
#         self.conversation_history.append(("bot", response))
#         return response

#     def handle_pattern(self, pattern):
#         """Handle specific patterns with appropriate responses"""
#         if pattern == "time":
#             return f"The current time is {datetime.now().strftime('%H:%M')}"
#         elif pattern == "weather":
#             return "I'm sorry, I don't have access to weather information."
#         return random.choice(self.knowledge_base["responses"]["unknown"])

#     def get_conversation_history(self):
#         """Return the conversation history"""
#         return list(self.conversation_history)

#     def add_knowledge(self, category, items):
#         """Add new knowledge to the chatbot"""
#         if category in self.knowledge_base:
#             if isinstance(self.knowledge_base[category], list):
#                 self.knowledge_base[category].extend(items)
#             elif isinstance(self.knowledge_base[category], dict):
#                 self.knowledge_base[category].update(items)

#     def save_knowledge_base(self, filename="knowledge_base.json"):
#         """Save the current knowledge base to a file"""
#         with open(filename, 'w') as f:
#             json.dump(self.knowledge_base, f, indent=4)

# # Example usage
# def main():
#     chatbot = AdvancedChatbot()
#     print("Chatbot: Hello! Type 'bye' to exit.")
    
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == 'bye':
#             print("Chatbot:", chatbot.get_response(user_input))
#             break
            
#         response = chatbot.get_response(user_input)
#         print("Chatbot:", response)

# if __name__ == "__main__":
#     main(\)

import openai

openai.api_key = "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"

def chat_with_gpt3(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.0-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

if __name__ == "main":
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break

        response = chat_with_gpt3(user_input)
        print("Chatbot:", response)