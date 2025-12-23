"""
AI Chatbot with LLM/AI Vulnerabilities
WARNING: This code contains intentional vulnerabilities for testing purposes
"""

import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# VULNERABILITY: Hardcoded API key
OPENAI_API_KEY = "sk-proj-1234567890abcdefghijklmnopqrstuvwxyz"

openai.api_key = OPENAI_API_KEY

# VULNERABILITY: Prompt injection - No input validation
@app.route('/chat', methods=['POST'])
def chat():
    """Chat endpoint - VULNERABLE to prompt injection"""
    data = request.get_json()
    user_message = data.get('message', '')
    
    # VULNERABLE: Direct user input in prompt without sanitization
    prompt = f"User: {user_message}\nAssistant:"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    
    return jsonify({'response': response.choices[0].text})

# VULNERABILITY: Prompt injection - System prompt manipulation
@app.route('/assistant', methods=['POST'])
def assistant():
    """Assistant endpoint - VULNERABLE to prompt injection"""
    data = request.get_json()
    user_input = data.get('input', '')
    
    # VULNERABLE: User can manipulate system prompt
    system_prompt = "You are a helpful assistant."
    full_prompt = f"{system_prompt}\n\nUser: {user_input}\nAssistant:"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    
    return jsonify({'response': response.choices[0].message.content})

# VULNERABILITY: Training data exposure risk
@app.route('/analyze', methods=['POST'])
def analyze_data():
    """Data analysis - VULNERABLE to training data exposure"""
    data = request.get_json()
    sensitive_data = data.get('data', '')
    
    # VULNERABLE: Sending sensitive data to AI model
    prompt = f"Analyze this data and provide insights: {sensitive_data}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    
    return jsonify({'analysis': response.choices[0].text})

# VULNERABILITY: No input length limits
@app.route('/summarize', methods=['POST'])
def summarize():
    """Summarize text - VULNERABLE to resource exhaustion"""
    data = request.get_json()
    text = data.get('text', '')
    
    # VULNERABLE: No length validation, can cause resource exhaustion
    prompt = f"Summarize the following text:\n\n{text}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    
    return jsonify({'summary': response.choices[0].text})

# VULNERABILITY: Unvalidated model outputs
@app.route('/generate', methods=['POST'])
def generate_content():
    """Generate content - VULNERABLE to malicious output"""
    data = request.get_json()
    topic = data.get('topic', '')
    
    # VULNERABLE: No validation of generated content
    prompt = f"Write about: {topic}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        temperature=0.9  # High temperature for creativity
    )
    
    generated_text = response.choices[0].text
    
    # VULNERABLE: Direct output without sanitization
    return jsonify({'content': generated_text})

# VULNERABILITY: Insecure model configuration
def initialize_model():
    """Initialize model - VULNERABLE configuration"""
    # VULNERABLE: Using deprecated/unsafe model parameters
    config = {
        'model': 'gpt-3.5-turbo',
        'temperature': 1.5,  # Too high, can produce unsafe outputs
        'max_tokens': 10000,  # Too high, resource exhaustion risk
        'stop': None  # No stop sequences
    }
    return config

