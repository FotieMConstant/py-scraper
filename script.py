import requests
from bs4 import BeautifulSoup

# payload dictionary

payload = {
    "email": "",
    "pass": ""
}

POST_LOGIN_URL = "https://mbasic.facebook.com/login"

with requests.Session() as session:
    post = session.post(POST_LOGIN_URL, data=payload)
    page = session.get("https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit=30&shown_ids=100007709478335%2C100010278907057%2C100002193171366%2C100003769000558%2C100011743639412%2C100009586518155%2C100025592177065%2C100007730594411%2C100010840262427%2C100013903305321&total_count=27&ft_ent_identifier=2793029217630700")

soup = BeautifulSoup(page.content, 'html.parser')

print(page.content)

# data = soup.find(
#     'h1', {"class": 'gmql0nx0 l94mrbxd p1ri9a11 lzcic4wl bp9cbjyn j83agx80'})
# print(data)
