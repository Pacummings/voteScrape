
class Senator:

	def __init__(self, name, party, state):
		self.name = name
		self.voting_record = {}
		self.state = state
		self.party = party

	def add_vote(self, vote_obj, vote):
		self.voting_record[vote_obj] = vote

class Vote:
	def __init__(self):
		self.yeas = {}
		self.nays = {}

	def set_identifier(self,congress_number,session,vote_number):
		self.congress_number = congress_number
		self.session = session
		self.vote_number = vote_number		

	def set_date(self,day,month,year):
		self.day = day
		self.month = month
		self.year = year

	def set_description(self,description):
		self.description = description

	def set_issue(self,issue):
		self.issue = issue

	def add_yea(self,senator):
		if senator not in self.yeas:
			self.yeas[senator.name] = senator

	def add_nay(self,senator):
		if senator not in self.nays:
			self.nays[senator.name] = senator