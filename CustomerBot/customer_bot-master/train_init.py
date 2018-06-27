'''
generates dialogue management model, stored in model_path
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

if __name__ == '__main__':
	logging.basicConfig(level='INFO')

	training_data_file = 'C:/Murali/Testing/hackathon2018/customer_bot-master/data/stories.md'
	model_path = 'C:/Murali/Testing/hackathon2018/customer_bot-master/models/dialogue'

	agent = Agent('customer_domain.yml', policies = [MemoizationPolicy(), KerasPolicy()])

	agent.train(
			training_data_file,
			epochs = 500,
			batch_size = 10,
			validation_split = 0.2)

	agent.persist(model_path)
