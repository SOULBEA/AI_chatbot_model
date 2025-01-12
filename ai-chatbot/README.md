# AI Chatbot with 3D Character Model

This project implements an AI chatbot displayed through a 3D character model using web technologies and Streamlit. The chatbot interacts with users via voice input and provides responses with synchronized lip movements.

## Project Structure

```
ai-chatbot
├── src
│   ├── app.py                # Main entry point of the Streamlit application
│   ├── chatbot
│   │   └── chatbot.py        # Logic for the AI chatbot
│   ├── static
│   │   ├── model.vrm         # 3D character model in VRM format
│   │   └── background.jpg     # Custom background image
│   └── templates
│       └── index.html        # HTML structure for the main page
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Features

- **Voice Interaction**: Users can interact with the chatbot using their microphone.
- **3D Character Model**: A VRM model represents the chatbot visually.
- **Lip Syncing**: The character model's lips sync with the chatbot's responses.
- **Custom Background**: A personalized background enhances the user experience.
- **Resizable and Draggable Window**: The application window can be resized and moved.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-chatbot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run src/app.py
   ```

## Usage Guidelines

- Ensure your microphone is set up and permissions are granted for the application to access it.
- Speak clearly into the microphone to interact with the chatbot.
- Enjoy the conversation with the 3D character model!

## Acknowledgments

This project utilizes various libraries for AI processing, audio handling, and 3D model rendering. Please refer to the `requirements.txt` for a complete list of dependencies.