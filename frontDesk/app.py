# Murali
from flask import Flask
from flask import render_template, jsonify, request
import requests
# from models import *
import random
from frontdesk_util import front_response

app = Flask(__name__)
app.secret_key = '12345'


@app.route('/')
def hello_world():
    return render_template('home-SELECT.html')


@app.route('/chat', methods=["POST"])
def chat():
    try:
        user_message = request.form["text"]
        # should return the response to be
        response = front_response(user_message)
        
        return jsonify({"status": "success", "response": response})
    except Exception as e:
        print(e)
        return jsonify({"status": "success", "response": "Apologies! I am yet to be trained to respond to this query..."})


app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8081)
