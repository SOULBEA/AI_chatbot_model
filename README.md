# AI Chatbot Model

This project is a web-based AI chatbot model that includes a 3D scene rendered using Three.js. The chatbot interface includes a typing indicator, message container, and input field for user interaction. Additionally, the 3D model blinks every 3 seconds to simulate a more lifelike appearance.

## Features

- 3D scene rendered using Three.js
- Chat interface with typing indicator and message container
- Blinking animation for the 3D model every 3 seconds

## Getting Started

### Prerequisites

To run this project, you need a web browser that supports HTML5, CSS3, and JavaScript.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/ai-chatbot-model.git
    ```
2. Navigate to the project directory:
    ```sh
    cd ai-chatbot-model
    ```

### Usage

1. Open the `index.html` file in your web browser:
    ```sh
    open index.html
    ```
    or simply double-click the `index.html` file.

2. Interact with the chatbot by typing messages in the input field and clicking the send button.

## Code Overview

### HTML

The main structure of the project is defined in the `index.html` file. It includes the 3D scene container, chat overlay, and input field.

### CSS

The styles for the project are included within the `<style>` tags in the `index.html` file. It defines the layout and appearance of the chat interface and the blinking animation.

### JavaScript

The JavaScript code is included within the `<script>` tags in the `index.html` file. It initializes the Three.js renderer and sets up the blinking animation for the 3D model.

#### Blinking Animation

The blinking animation is defined using CSS keyframes and is triggered every 3 seconds using JavaScript.

