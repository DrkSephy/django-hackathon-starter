# pylint: disable=line-too-long

'''
scraper.py contains various methods for scraping
HTML content and packaging into dictionaries.
'''

import requests
from bs4 import BeautifulSoup

def fetchHTML(url):
    '''
    Returns HTML retrived from a url.

    Parameters:
        url: String
            - The URL to fetch HTML from

    Returns:
        html: String
            - The HTML from a given URL
    '''
    req = requests.get(url)
    html = req.text
    return html

def extractTag(content, tag, className=None):
    '''
    Returns data embed within a tag, along
    with an optional class for filtering.

    Parameters:
        content: String
            - The HTML to parse
        tag: String
            - The HTML tag to scan for
        class: String
            - Optional filter for tag

    Returns:
        filteredData: List
            - Content embed within searched tags
    '''
    soup = BeautifulSoup(content)
    data = soup.findAll(tag, {'class': className})
    filteredData = []
    for datum in data:
        filteredData.append(datum.text)
    return filteredData


def steamDiscounts():
    '''Returns discounts from steam.com'''
    req = requests.get('http://store.steampowered.com/search/?specials=1#sort_by=_ASC&sort_order=ASC&specials=1&page=1')
    content = req.text
    soup = BeautifulSoup(content)
    allData = {id: {} for id in range(0, 25)}

    # Get all divs of a specific class
    releaseDate = soup.findAll('div', {'class': 'col search_released'})

    # Get all release dates
    releaseDates = []
    id = 0
    for date in releaseDate:
        allData[id]['releaseDates'] = date.text
        releaseDates.append(date.text)
        id += 1

    #print releaseDates

    id = 0
    gameName = soup.findAll('div', {'class': 'col search_name ellipsis'})

    # Get all game names
    gameNames = []
    for name in gameName:
        span = name.findAll('span', {'class': 'title'})
        for tag in span:
            allData[id]['name'] = tag.text
            gameNames.append(tag.text)
            id += 1

    # print gameNames

    discount = soup.findAll('div', {'class': 'col search_discount'})

    id = 0
    # Get all game discounts
    gameDiscounts = []
    for discountedGame in discount:
        span = discountedGame.findAll('span')
        for tag in span:
            allData[id]['discount'] = tag.text
            gameDiscounts.append(tag.text)
            id += 1

    # print gameDiscounts

    price = soup.findAll('div', {'class': 'col search_price discounted'})

    id = 0
    prices = []
    # Get all discounted prices
    for value in price:
        br = value.findAll('br')
        for tag in br:
            allData[id]['price'] = tag.text.strip('\t')
            prices.append(tag.text.strip('\t'))
            id += 1

    # Cleanup data
    newData = []
    for datum in allData:
        newData.append(allData[datum])
    # print prices
    return newData




