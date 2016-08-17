from bs4 import BeautifulSoup
import urllib
from senator import *
import re

votes = []
senators = {}

#Input your own numbers
congress_number = 114
session = 2

#This opens a page containing an overview of all
#votes that occurred in this congress number and session
s = urllib.urlopen("http://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_{}_{}.htm".format(congress_number,session))
vote_soup = BeautifulSoup(s)

#vote_page_text breaks up the webpage by the number of bills
#The first piece of text contains the headers
vote_page_text = vote_soup.find_all("tr")
num_votes = len(vote_page_text)-1

#vote_page_text_td breaks up the webpage by the attributes
#For each bill there is:
#	1. Vote (Tally)
#	2. Result
#	3. Description
#	4. Issue
#	5. Date
vote_page_text_td = vote_soup.find_all("td")

for i in range(1,num_votes+1):

	try:
		vote_num = num_votes-i+1
		print vote_num

		current_vote = Vote()
		current_vote.set_identifier(congress_number,session,vote_num)
		
		bill_vote = vote_page_text_td[i*5].get_text()
		bill_vote_match = re.match('([0-9]*)\xa0\(([0-9]*)-([0-9]*)\)',bill_vote)

		votes_yea = bill_vote_match.group(2)
		votes_nay = bill_vote_match.group(3)

		bill_result = vote_page_text_td[i*5+1].get_text()

		bill_desc = vote_page_text_td[i*5+2].get_text()
		current_vote.set_description(bill_desc)

		bill_issue = vote_page_text_td[i*5+3].get_text()
		current_vote.set_issue(bill_issue)

		bill_date = vote_page_text_td[i*5+4].get_text()

		votes.insert(0,current_vote)	

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
				senators[senator_name].add_vote(current_vote,senator_vote)

				if senator_vote=='Yea':
					current_vote.add_yea(senators[senator_name])
				elif senator_vote=='Nay':
					current_vote.add_nay(senators[senator_name])


	except:
		print "Could not load vote number "+str(vote_num)
		pass





