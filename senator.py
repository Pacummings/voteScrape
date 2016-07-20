
class Senator:

	def __init__(self, name, party, state):
		self.name = name
		self.voting_record = {}
		self.state = state
		self.party = party

	def add_vote(self, bill, vote):
		self.voting_record[bill] = vote
