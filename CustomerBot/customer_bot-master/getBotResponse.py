#Murali
from flask import Flask
from flask import render_template,jsonify,request
import requests
# from models import *
from engine import *
import random
app = Flask(__name__)
app.secret_key = '12345'

@app.route("/getBotResponse",methods=["POST"])
def getChatResponse(user_message):
    print(user_message)
    response = requests.get("http://localhost:5000/parse",params={"q":user_message})
    response = response.json()
    entities = response.get("entities")
    topresponse = response["topScoringIntent"]
    intent = topresponse.get("intent")
    print("Intent {}, Entities {}".format(intent,entities))
    if intent == "event-name":
        response_text = hr_info(entities)
    elif intent == "event-name":
        response_text = req_query(entities)
    else:
        response_text = get_random_response(intent)
    return response_text
    
    
