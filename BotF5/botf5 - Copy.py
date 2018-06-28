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

logger = logging.getLogger(__name__)

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
	
	if serve_forever:
		agent.handle_channel(ConsoleInputChannel())
		print(agent)

	return agent

if __name__ == '__main__':
	#train_dialogue()
	run_customer_bot()
