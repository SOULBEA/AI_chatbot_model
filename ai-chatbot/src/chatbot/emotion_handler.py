from textblob import TextBlob
import re

class EmotionHandler:
    def __init__(self):
        self.emotion_patterns = {
            'joy': r'\b(happy|great|awesome|wonderful|love|excited|:D|😊|😃)\b',
            'sadness': r'\b(sad|sorry|upset|unhappy|disappointed|😢|😔)\b',
            'anger': r'\b(angry|mad|hate|furious|annoyed|😠|😡)\b',
            'surprise': r'\b(wow|omg|really|surprised|amazing|😮|😲)\b',
            'neutral': r'\b(okay|fine|alright|normal|🙂)\b'
        }

    def analyze_emotion(self, text):
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        detected_emotions = []
        for emotion, pattern in self.emotion_patterns.items():
            if re.search(pattern, text.lower()):
                detected_emotions.append(emotion)

        if detected_emotions:
            dominant_emotion = detected_emotions[0]
        else:
            if sentiment > 0.3:
                dominant_emotion = 'joy'
            elif sentiment < -0.3:
                dominant_emotion = 'sadness'
            else:
                dominant_emotion = 'neutral'

        confidence = abs(sentiment) if abs(sentiment) > 0.5 else 0.5

        return {
            'emotion': dominant_emotion,
            'confidence': confidence
        } 