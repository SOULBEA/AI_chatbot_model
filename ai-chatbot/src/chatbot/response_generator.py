import random
import emoji

class ResponseGenerator:
    def __init__(self):
        self.responses = {
            'joy': ["That's wonderful! 😊", "I'm glad to hear that! 💖", "Yay! 🎉"],
            'sadness': ["I'm here for you. 💔", "I understand, it's tough. 😢", "Let me know if I can help. 😔"],
            'anger': ["Let's take a deep breath. 🌸", "I'm here to listen. 💢", "I understand your frustration. 😤"],
            'surprise': ["Wow, that's interesting! 😮", "Tell me more! ✨", "Really? That's amazing! 😲"],
            'neutral': ["I'm listening. 🌟", "Tell me more. 💭", "Go on, I'm here. 🙂"]
        }

    def generate_response(self, user_input, emotion_data):
        emotion = emotion_data['emotion']
        response = random.choice(self.responses.get(emotion, self.responses['neutral']))
        return self.add_emotional_expressions(response, emotion)

    def add_emotional_expressions(self, text, emotion):
        emotion_expressions = {
            'joy': ['😊', '💖', '✨'],
            'sadness': ['😔', '💔', '😢'],
            'anger': ['😠', '💢', '😤'],
            'surprise': ['😮', '😲', '✨'],
            'neutral': ['🙂', '💭', '✨']
        }

        expressions = emotion_expressions.get(emotion, emotion_expressions['neutral'])
        if len(text) > 50:
            text = f"{expressions[0]} {text}"
            if '.' in text:
                text = text.replace('.', f' {expressions[1]}.', 1)

        return text 