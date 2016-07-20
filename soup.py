from bs4 import BeautifulSoup
import urllib.request
r = urllib.request.urlopen('http://www.senate.gov/pagelayout/legislative/a_three_sections_with_teasers/votes.htm').read()
soup = BeautifulSoup(r)
print type(soup)