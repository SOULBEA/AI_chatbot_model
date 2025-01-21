import re
import random
from collections import defaultdict
from typing import List, Dict, Tuple, Optional

class AdvancedChatbot:
    def __init__(self):
        # Initialize response patterns and their corresponding responses
        self.patterns = {
            r'hello|hi|hey': [
                'Hello! How can I help you today?',
                'Hi there! What brings you here?',
                'Hey! What can I do for you?'
            ],
            r'how are you': [
                "I'm doing well, thank you for asking! How about you?",
                "I'm great! How are you doing?",
                "Doing fine, thanks! And yourself?"
            ],
            r'bye|goodbye': [
                'Goodbye! Have a great day!',
                'See you later! Take care!',
                'Bye! Come back soon!'
            ],
            r'what is your name': [
                "I'm ChatBot, nice to meet you!",
                "You can call me ChatBot!",
                "The name's ChatBot!"
            ],
            r'help|support': [
                "I can help you with general questions, basic tasks, and friendly conversation. What do you need?",
                "I'm here to assist! What kind of help are you looking for?",
                "Sure, I'd be happy to help! What's on your mind?"
            ]
        }
        
        # Context memory
        self.context = {
            'user_name': None,
            'last_topic': None,
            'conversation_history': []
        }
        
        # Sentiment keywords
        self.sentiment_words = {
            'positive': ['good', 'great', 'excellent', 'amazing', 'wonderful', 'happy', 'love'],
            'negative': ['bad', 'terrible', 'awful', 'horrible', 'sad', 'hate', 'poor'],
            'neutral': ['okay', 'fine', 'alright', 'normal']
        }

    def preprocess_input(self, user_input: str) -> str:
        """Preprocess the user input by converting to lowercase and removing extra whitespace."""
        return ' '.join(user_input.lower().split())

    def analyze_sentiment(self, text: str) -> str:
        """Analyze the sentiment of the input text."""
        words = text.lower().split()
        
        pos_count = sum(1 for word in words if word in self.sentiment_words['positive'])
        neg_count = sum(1 for word in words if word in self.sentiment_words['negative'])
        
        if pos_count > neg_count:
            return 'positive'
        elif neg_count > pos_count:
            return 'negative'
        return 'neutral'

    def extract_user_name(self, text: str) -> Optional[str]:
        """Extract user name from input if mentioned."""
        name_patterns = [
            r'my name is (\w+)',
            r"i'm (\w+)",
            r'i am (\w+)',
            r'call me (\w+)'
        ]
        
        for pattern in name_patterns:
            match = re.search(pattern, text.lower())
            if match:
                return match.group(1).capitalize()
        return None

    def generate_response(self, user_input: str) -> str:
        """Generate a response based on user input and context."""
        processed_input = self.preprocess_input(user_input)
        
        # Update context
        self.context['conversation_history'].append(('user', processed_input))
        
        # Extract name if mentioned
        name = self.extract_user_name(processed_input)
        if name:
            self.context['user_name'] = name
            return f"Nice to meet you, {name}! How can I help you today?"

        # Check for pattern matches
        for pattern, responses in self.patterns.items():
            if re.search(pattern, processed_input):
                response = random.choice(responses)
                
                # Personalize response if we know the user's name
                if self.context['user_name'] and random.random() < 0.3:  # 30% chance to use name
                    response = f"{self.context['user_name']}, {response}"
                
                self.context['conversation_history'].append(('bot', response))
                return response

        # Handle unknown inputs based on sentiment
        sentiment = self.analyze_sentiment(processed_input)
        if sentiment == 'positive':
            response = "I'm glad you're feeling positive! What would you like to talk about?"
        elif sentiment == 'negative':
            response = "I sense you might be feeling down. Is there something specific you'd like to discuss?"
        else:
            response = "I'm not sure I understand. Could you please rephrase that or ask me something specific?"

        self.context['conversation_history'].append(('bot', response))
        return response

    def get_conversation_history(self) -> List[Tuple[str, str]]:
        """Return the conversation history."""
        return self.context['conversation_history']

# Example usage
def chat():
    chatbot = AdvancedChatbot()
    print("ChatBot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye', 'exit']:
            print("ChatBot:", chatbot.generate_response(user_input))
            break
        
        response = chatbot.generate_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    chat()