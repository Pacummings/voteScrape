from bs4 import BeautifulSoup
import urllib
import senator
import re

r = urllib.urlopen("http://www.senate.gov/legislative/LIS/roll_call_lists/roll_call_vote_cfm.cfm?congress=114&session=2&vote=00134")

soup = BeautifulSoup(r)
letters = soup.find_all("td", class_="contenttext")

correct_index = -1

for i in range(len(letters)):
	current_text = letters[i].get_text()
	if current_text == 'By Home State':
		correct_index = i
		break

voting_text = ''
for i in range(1,4):
	voting_text += letters[correct_index+i].get_text()

voting_text = voting_text.split('\n')

senators = []

for line in voting_text:
	line = line.strip()
	match_obj = re.match('(\w+)\s\\((\w)-(\w+)\\),\s(\w+\s*\w*)',line)

	if match_obj: 
		s = senator.Senator(match_obj.group(1),match_obj.group(2),match_obj.group(3))
		senators.append(s) 
