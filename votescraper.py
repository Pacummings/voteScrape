from bs4 import BeautifulSoup
import urllib

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

print voting_text





