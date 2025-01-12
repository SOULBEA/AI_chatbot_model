from flask import Flask, render_template, jsonify, request, send_from_directory
import speech_recognition as sr
import pyttsx3
import os
import random

app = Flask(__name__, static_folder='static')

# Simple response dictionary
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm doing great, thanks!", "I'm fine, how are you?", "All good!"],
    "what's your name": ["I'm your AI assistant!", "You can call me AI!", "I'm your virtual friend!"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "default": ["Interesting!", "Tell me more about that.", "I understand.", "I see."]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/process_speech', methods=['POST'])
def process_speech():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5)
            user_input = recognizer.recognize_google(audio)
            
            # Generate chatbot response
            response = generate_response(user_input.lower())
            
            # Text to speech with female voice
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            # Set female voice (usually index 1 is female)
            engine.setProperty('voice', voices[1].id)
            # Adjust speech rate and volume
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 0.9)
            engine.say(response)
            engine.runAndWait()
            
            return jsonify({
                "status": "success",
                "user_input": user_input,
                "response": response
            })
            
    except sr.UnknownValueError:
        return jsonify({"status": "error", "message": "Could not understand audio"})
    except sr.RequestError:
        return jsonify({"status": "error", "message": "Could not request results"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

def generate_response(user_input):
    # Check for keywords in user input
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    # If no keyword matches, return default response
    return random.choice(responses["default"])

if __name__ == '__main__':
    app.run(debug=True)