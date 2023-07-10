from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()
resp = session.get('https://www.laufen.co.at/produkte/waschtische-wandhangend', timeout=10)
soup = BeautifulSoup(resp.html.html, 'lxml')

# Before rendering
print("Before Rendering : ", len(soup.find_all('h3', {'class': 'title-producto'})))

resp.html.render(timeout=20)
soup = BeautifulSoup(resp.html.html, 'lxml')

# After rendering
print("After Rendering : ", len(soup.find_all('h3', {'class': 'title-producto'})))
