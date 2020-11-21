import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://github.com/FotieMConstant/')
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(
    'span', {"class": 'p-name vcard-fullname d-block overflow-hidden'})
print(week.string)
