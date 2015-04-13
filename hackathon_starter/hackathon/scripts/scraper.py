import requests
from bs4 import BeautifulSoup

req = requests.get('http://store.steampowered.com/search/?specials=1#sort_by=_ASC&sort_order=ASC&specials=1&page=1')
content = req.text
soup = BeautifulSoup(content)

# Get all divs of a specific class
releaseDate = soup.findAll('div', {'class': 'col search_released'})

# Get all release dates
releaseDates = []
for date in releaseDate:
	releaseDates.append(date.text)

print releaseDates