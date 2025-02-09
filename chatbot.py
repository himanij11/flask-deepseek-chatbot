import re
from flask import Flask, render_template, request
from langchain_ollama import ChatOllama  
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)

chat_history = []

@app.route('/')
def home():
    return render_template('index.html')

def generate_response_llm(question):

    template = """
    Answer the questions asked. Do not give funny responses. Respond briefly.

    Here is the conversation history: {chat_history}

    Question: {question}
    
    Answer:

    """

    prompt = ChatPromptTemplate.from_template(template)
    model = ChatOllama(model = "deepseek-r1:7b", base_url = "http://host.docker.internal:11434")
    chain = prompt | model 

    response = chain.invoke({"chat_history": chat_history, "question": question})
    cleaned_response = re.sub(r'<think>.*?</think>', '', response.content, flags = re.DOTALL).strip()
    chat_history.append({"question": question, "response": cleaned_response})

    return cleaned_response

@app.route('/get', methods=["GET", "POST"])
def chatbot_response():
    userText = request.args.get('msg') if request.method == "GET" else request.form.get('msg')
    response = generate_response_llm(userText)
    return str(response)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 8080)