# Flask Chatbot with Ollama Integration
A web-based chatbot application built with Flask and integrated with Ollama's language models. 
The chatbot provides a clean, responsive interface for users to interact with AI models through a simple chat interface.

## Project Structure

```
.
├── chatbot.py           # Main Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
└── templates/
    └── index.html     # Main chat interface
```

## Prerequisites

- Python 3.x
- Docker (for containerized deployment)
- Ollama running locally with DeepSeek model

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/himanij11/flask-deepseek-chatbot.git
cd flask-deepseek-chatbot
```

### 2. Set Up Virtual Environment

Create a virtual environment using the following commands:

```bash
python3 -m venv chatbot
```

Activate the virtual environment:

- On macOS/Linux:

  ```bash
  source chatbot/bin/activate
  ```

- On Windows:

  ```bash
  chatbot\Scripts\activate
  ```


### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run Ollama locally

Ensure Ollama is running locally with the `deepseek-r1:7b` model. You can start Ollama using:

```bash
ollama serve
```

```bash
ollama run deepseek-r1:7b
```

## Running the Application

### Using Docker

1. Build the Docker image:
```bash
docker build -t chatbot_app .
```

2. Run the container:
```bash
docker run -p 8080:8080 chatbot_app
```

## Configuration

The chatbot is configured to use the DeepSeek model through Ollama. You can modify the model and other settings in `chatbot.py`:

```python
model = ChatOllama(
    model="deepseek-r1:7b",
    base_url="http://host.docker.internal:11434"
)
```

## Usage

1. Open your browser and navigate to `http://localhost:8080/` or `http://127.0.0.1:8080/` 
2. Interact with the chatbot using the provided interface.
