from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import sqlite3 

class ActionProvideReport(Action):
	def name(self):
		return 'action_provide_report'

	def run(self, dispatcher, tracker, domain):

		#prod = tracker.get_slot('product')
		#router = tracker.get_slot('router')
		recs = tracker.get_slot('recs')
		confirmationNumber = All #later generate through some process

		#response = """Your product {} is ordered for you. It will be shipped to your address. Your confirmation number is {}""".format(router, confirmationNumber)
		
		response = """You re in provide report- here Pull report from DB and feed it to the bot""".format(recs, confirmationNumber)

		dispatcher.utter_message(response)
		return [SlotSet('router',router)]
		
		
class ActionApproveRec(Action):
	def name(self):
		return 'action_approve_rec'

	def run(self, dispatcher, tracker, domain):

		#prod = tracker.get_slot('product')
		router = tracker.get_slot('router')
		confirmationNumber = 123456 #later generate through some process

		response = """Your are in approve rec- here you approve records which are open  or specific record"""

		dispatcher.utter_message(response)
		return [SlotSet('router',router)]

class ActionInBMOApproveRecs(Action):
	def name(self):
		return 'action_InBMOApprove_Recs'

	def run(self, dispatcher, tracker, domain):

		#prod = tracker.get_slot('product')
		router = tracker.get_slot('router')
		confirmationNumber = 123456 #later generate through some process
		
		conn = sqlite3.connect("PX_DB_Demo")
		reqs = conn.execute("select reqID, skillset, position, status, lob from PX_Requirements where status='InBMOApproval'")
		for row in reqs:
			print("ReqID = ", row[0], " Skillset = ", row[1], " Position =", row[2], " Status =", row[3], " LOB =", row[4])
		response = """Your are in InBMOApproveRecs- here you list all records which are in InBMOapproverecs accross LOBs \n "ReqID = ", row[0], " Skillset = ", row[1], " Position =", row[2], " Status =", row[3], " LOB =", row[4]"""
		
		dispatcher.utter_message(response)
		return [SlotSet('router',router)]

		
class ActionCreateRecID(Action):
	def name(self):
		return 'action_create_recID'

	def run(self, dispatcher, tracker, domain):

		#prod = tracker.get_slot('product')
		recs = tracker.get_slot('recs')
		confirmationNumber = 123456 #later generate through some process

		response = """Your are in creating rec ID"""

		dispatcher.utter_message(response)
		return [SlotSet('recs',recs)]
		
class ActionGetMatchingProfilesForRecID(Action):
	def name(self):
		return 'action_approve_rec'

	def run(self, dispatcher, tracker, domain):

		#prod = tracker.get_slot('product')
		recs = tracker.get_slot('recs')
		confirmationNumber = 123456 #later generate through some process

		response = """Your are in in matching profileFor"""

		dispatcher.utter_message(response)
		return [SlotSet('recs',recs)]