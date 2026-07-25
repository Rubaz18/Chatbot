# Simple AI Chatbot

## Project Overview

This project is a simple AI chatbot developed using **Python** and **Flask**. It can interact with users by telling jokes, solving mathematical expressions, and answering general questions. If an OpenAI API key is available, the chatbot provides AI-generated responses. Otherwise, it uses a local fallback system to respond to users.

The project was developed to learn the basics of chatbot development, web applications using Flask, and API integration.

---

# Objective

The objective of this project is to develop a simple AI chatbot using Flask that can communicate with users, perform mathematical calculations safely, tell jokes, and provide general assistance. The project also demonstrates how a chatbot can work with or without an AI API.

---

# Features

* Tell jokes (Example: **"tell me a joke"**)
* Solve mathematical calculations (Example: **2+2**, **sqrt(16)**)
* AI-generated responses using the OpenAI API (optional)
* Local fallback responses when no API key is available
* Simple and user-friendly web interface
* Safe evaluation of mathematical expressions

---

# Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* OpenAI API (Optional)
* Waitress

---

# Required Libraries

Install the following Python libraries before running the project:

* Flask
* OpenAI
* Waitress

Or simply install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# Project Structure

```text
Chatbot/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── render.yaml
├── fly.toml
├── templates/
├── static/
└── README.md
```

---

# Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/Rubaz18/Chatbot.git
cd Chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install the required libraries

```bash
pip install -r requirements.txt
```

### 5. (Optional) Set the OpenAI API Key

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

This step is optional. If you do not provide an API key, the chatbot will use its local fallback responses.

---

# How to Run the Project

Start the Flask server using:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

You can now interact with the chatbot through the web interface.

---

# Example Commands

* tell me a joke
* 2 + 2
* 10 * 5
* sqrt(49)
* Explain Python loops.
* What is Artificial Intelligence?

---

# How It Works

* The chatbot receives the user's message.
* It detects the user's intent.
* If the user requests a joke, it returns a random joke.
* If the user enters a mathematical expression, the chatbot safely evaluates it using Python AST.
* If an OpenAI API key is available, the chatbot uses the OpenAI API to answer general questions.
* If no API key is available, the chatbot provides local fallback responses.

---

# Expected Output

After running the project:

1. The Flask server starts successfully.
2. The application becomes available at **http://127.0.0.1:5000**.
3. The chatbot interface is displayed in the browser.
4. Users can ask for jokes, perform mathematical calculations, and ask general questions.
5. The chatbot responds according to the user's request.

---

# Deployment

The chatbot can also be deployed on cloud platforms such as:

* Render
* Fly.io
* Railway

You can also build and run the project using Docker.

```bash
docker build -t chatbot .
docker run -p 5000:5000 chatbot
```

---

# Future Improvements

* Add more chatbot intents
* Improve the user interface
* Store chat history
* Add voice input and output
* Support multiple languages
* Improve AI capabilities
* Add user authentication

---

# Author

**Rubaz Khan**

BS Computer Science

---

# License

This project was developed for educational and learning purposes.
