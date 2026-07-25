# Simple AI Chatbot

## Project Overview

This is a simple AI chatbot built using **Python** and **Flask**. It provides basic chatbot features such as telling jokes, solving math expressions, and answering questions. If an OpenAI API key is available, the chatbot can generate AI-powered responses. Otherwise, it uses a local fallback system.

This project was created for learning purposes and to understand how chatbots work with Flask and Python.

---

# Features

* Tell jokes (Example: **"tell me a joke"**)
* Solve math calculations (Example: **2+2**, **sqrt(16)**)
* AI responses using OpenAI (when an API key is provided)
* Local fallback responses if no API key is available
* Simple web interface using Flask

---

# Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* OpenAI API (Optional)

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

# Installation

### 1. Clone the repository

```bash
git clone <repository-link>
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

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. (Optional) Add your OpenAI API Key

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

### 6. Run the chatbot

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# Example Commands

* tell me a joke
* 5 + 10
* sqrt(49)
* What is Artificial Intelligence?
* Explain Python loops.

---

# How It Works

* The chatbot checks what the user types.
* If it is a math expression, it solves it using a safe Python evaluator.
* If the user asks for a joke, it returns a random joke.
* If an OpenAI API key is available, it uses AI to answer general questions.
* If no API key is provided, it gives a simple local response.

---

# Deployment

This project can be deployed on cloud platforms such as:

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
* Support more AI features
* Add user authentication

---

# Author

**Rubaz Khan**

BS Computer Science Student

---

# License

This project is created for educational and learning purposes.
