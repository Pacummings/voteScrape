from bs4 import BeautifulSoup
import urllib
from senator import *
import re

#Testing
bills = []
senators = {}

for vote_num in range(1,135):

	print vote_num

	current_bill = Bill(vote_num)
	bills.append(current_bill)

	#We first load the webpage
	r = urllib.urlopen("http://www.senate.gov/legislative/LIS/roll_call_lists/roll_call_vote_cfm.cfm?congress=114&session=2&vote="+"{0:0=5d}".format(vote_num))
	soup = BeautifulSoup(r)
	letters = soup.find_all("td", class_="contenttext")

	#We now find the list of senator votes
	#It follows after a string of text 'By Home State'
	correct_index = -1
	for i in range(len(letters)):
		current_text = letters[i].get_text()
		if current_text == 'By Home State':
			correct_index = i
			break

	#The next three lines seem to contain the voting info
	voting_text = ''
	for i in range(1,4):
		voting_text += letters[correct_index+i].get_text()

	#We now split it in to lines
	voting_text = voting_text.split('\n')

	#We find the senate votes
	for line in voting_text:
		line = line.strip()
		#The format will give Name, Party, State, Vote
		match_obj = re.match('(\w+)\s\\((\w)-(\w+)\\),\s(\w+\s*\w*)',line)

		if match_obj:
			senator_name = match_obj.group(1)
			senator_party = match_obj.group(2)
			senator_state = match_obj.group(3)
			senator_vote = match_obj.group(4)
			if senator_name not in senators.keys():
				s = Senator(senator_name, senator_party, senator_state)
				senators[senator_name] = s
			senators[senator_name].add_vote(current_bill,senator_vote)





