#Murali
from flask import Flask
from flask import render_template,jsonify,request
import requests
# from models import *
from engine import *
import random
import json
#from getBotResponse import *
app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def hello_world():
    return render_template('home-SELECT.html')

get_random_response = lambda intent:random.choice(intent_response_dict[intent])

@app.route('/chat',methods=["POST"])
def chat():
    try:
        user_message = request.form["text"]
        print(user_message)
        data1={"sender": "default", "message": user_message}
        print(data1)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response1 = requests.post("http://localhost:5005/chat/chat",data=json.dumps(data1),headers=headers)
        json_data = json.loads(response1.text)
        print(json_data)
        for no in json_data:
            print(no)
        return jsonify({"status":"success","response":no.get("text")})
    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})


app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)
