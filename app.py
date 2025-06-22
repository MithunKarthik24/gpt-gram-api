
from flask import Flask, request
import openai
import os

app = Flask(__name__)

# Load API key from environment variable (on Render, set it in settings)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/fix')
def fix():
    text = request.args.get('text', '')
    if not text:
        return "No input provided."

    # Send to GPT for grammar correction
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that corrects grammar and rephrases broken English into natural English."},
            {"role": "user", "content": f"Correct this sentence: {text}"}
        ],
        max_tokens=100,
        temperature=0.2
    )

    corrected = response['choices'][0]['message']['content'].strip()
    return corrected
