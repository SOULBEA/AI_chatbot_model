from flask import Flask, render_template, request, jsonify, send_from_directory
from chatbot.emotion_handler import EmotionHandler
from chatbot.response_generator import ResponseGenerator
import os

app = Flask(__name__, static_folder='static')

emotion_handler = EmotionHandler()
response_generator = ResponseGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_input = data['message']
        
        emotion_data = emotion_handler.analyze_emotion(user_input)
        response = response_generator.generate_response(user_input, emotion_data)
        
        return jsonify({
            'status': 'success',
            'response': response,
            'emotion': emotion_data['emotion']
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)