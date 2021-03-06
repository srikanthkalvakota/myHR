from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter

from flask import Flask
from flask import render_template,jsonify,request
import requests
# from models import *
from engine import *
import random
app = Flask(__name__)
app.secret_key = '12345'

logger = logging.getLogger(__name__)

@app.route('/')
def hello_world():
    return render_template('home-SELECT.html', data=[{'name':'Recruiter'},{'name':'HR-Manager'},{'name':'LOB-Head'}])

@app.route('/test', methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    print(select);
    if select == "Recruiter":
        return(render_template('Recruiter.html', data1='Recruiter'))
    elif select == "HR-Manager":
        return(render_template('HR-Manager.html', data1='HR-Manager'))
    elif select == "LOB-Head":
        return(render_template('LOB-Head.html', data1='LOB-Head'))

@app.route('/chat',methods=["POST"])
def chat():
    try:
        user_message = request.form["text"]
        response = requests.get("http://DESKTOP-NJ1L93T:5000/parse",params={"q":user_message})
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
        return jsonify({"status":"success","response":response_text})
    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"Apologies! I am yet to be trained to respond to this query..."})


def train_dialogue(domain_file = 'customer_domain.yml',
					model_path = 'C:/Srikanth/2018-Hackathon/git/myHR/CustomerBot/customer_bot-master/models/dialogue/',
					training_data_file = 'C:/Srikanth/2018-Hackathon/git/myHR/CustomerBot/customer_bot-master/data/stories.md'):

	agent = Agent(domain_file, policies = [MemoizationPolicy(), KerasPolicy()])

	agent.train(
				training_data_file,
				epochs = 300,
				batch_size = 50,
				validation_split = 0.2)

	agent.persist(model_path)
	return agent

def run_customer_bot(serve_forever=True):
	interpreter = RasaNLUInterpreter('C:/Srikanth/2018-Hackathon/git/myHR/CustomerBot/customer_bot-master/models/nlu/current/')
	agent = Agent.load('C:/Srikanth/2018-Hackathon/git/myHR/CustomerBot/customer_bot-master/models/dialogue/', interpreter = interpreter)
	app.run(port=8080)
	if serve_forever:
	    agent.handle_channel(ConsoleInputChannel())

	return agent

if __name__ == '__main__':
	#train_dialogue()
        run_customer_bot()
        #app.run(host="DESKTOP-NJ1L93T",port=8080)
        
