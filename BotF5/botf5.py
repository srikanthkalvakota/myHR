from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.channel import UserMessage
from rasa_core.channels.direct import CollectingOutputChannel
from rasa_core.channels.rest import HttpInputComponent
from flask import Blueprint, request, jsonify

logger = logging.getLogger(__name__)

class SimpleWebBot(HttpInputComponent):
    """A simple web bot that listens on a url and responds."""

    def blueprint(self, on_new_message):
        print('in blueprint');
        custom_webhook = Blueprint('custom_webhook', __name__)

        @custom_webhook.route("/status", methods=['GET'])
        def health():
            return jsonify({"status": "ok"})

        @custom_webhook.route("/chat", methods=['POST'])
        def receive():
            payload = request.json
            print(request)
            print('in receive bot')
            print(payload)
            sender_id = payload.get("sender", None)
            text = payload.get("message", None)
            print(text)
            out = CollectingOutputChannel()
            on_new_message(UserMessage(text, out, sender_id))
            print(out.messages)
##            responses = [m for _, m in out.messages]
            return jsonify(out.messages)
    
        return custom_webhook



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
	print(agent)

	input_channel = SimpleWebBot()
	if serve_forever:
		agent.handle_channel(HttpInputChannel(5005, "/chat", input_channel))
		print(agent)

	return agent

if __name__ == '__main__':
	#train_dialogue()
	run_customer_bot()
