#Python program to scrape website
#and save quotes from website
import requests
from bs4 import BeautifulSoup

URL = "https://www.daraz.pk/laptops/?spm=a2a0e.searchlistcategory.cate_7.5.1b74742cdOFlDu"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

images = soup.findAll('img')
src = []
for img in images:
    src.append(img['src'])

print(src)