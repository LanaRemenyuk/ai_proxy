import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
import openai

app = Flask(__name__)

load_dotenv()

openai.api_key = os.getenv('API_KEY')


@app.route('/get_response', methods=['POST'])
def get_answer():
    user_input = request.json['user_input']
    response = openai.Completion.create(
        engine='davinci',
        prompt=user_input,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.8
    )
    answer = response.choices[0].text.strip()

    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run()
