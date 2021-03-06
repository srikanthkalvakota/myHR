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



import random


app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def hello_world():
    return render_template('home.html')

#get_random_response = lambda intent:random.choice(intent_response_dict[intent])


@app.route('/chat',methods=["POST"])



logger = logging.getLogger(__name__)

def train_dialogue(domain_file = 'customer_domain.yml',
					model_path = 'C:/Murali/Testing/hackathon2018/customer_bot-master/models/dialogue/',
					training_data_file = 'C:/Murali/Testing/hackathon2018/customer_bot-master/data/stories.md'):

	agent = Agent(domain_file, policies = [MemoizationPolicy(), KerasPolicy()])

	agent.train(
				training_data_file,
				epochs = 300,
				batch_size = 50,
				validation_split = 0.2)

	agent.persist(model_path)
	return agent

def run_customer_bot(serve_forever=True):
	interpreter = RasaNLUInterpreter('C:/Murali/Testing/hackathon2018/customer_bot-master/models/nlu/current/')
	agent = Agent.load('C:/Murali/Testing/hackathon2018/customer_bot-master/models/dialogue/', interpreter = interpreter)

	if serve_forever:
		agent.handle_channel(ConsoleInputChannel())

	return agent

if __name__ == '__main__':
	#train_dialogue()
	run_customer_bot()
