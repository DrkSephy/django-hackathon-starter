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

gameName = soup.findAll('div', {'class': 'col search_name ellipsis'})

# Get all game names
gameNames = []
for name in gameName:
	span = name.findAll('span', {'class': 'title'})
	for tag in span:
		gameNames.append(tag.text)

print gameNames

discount = soup.findAll('div', {'class': 'col search_discount'})

# Get all game discounts 
gameDiscounts = []
for discountedGame in discount:
	span = discountedGame.findAll('span')
	for tag in span:
		gameDiscounts.append(tag.text)

print gameDiscounts

price = soup.findAll('div', {'class': 'col search_price discounted'})

prices = []
# Get all discounted prices
for value in price:
	br = value.findAll('br')
	for tag in br:
		prices.append(tag.text.strip('\t'))

print prices
