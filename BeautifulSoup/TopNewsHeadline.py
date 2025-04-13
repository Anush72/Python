# importing the libraries
from bs4 import BeautifulSoup
import requests

# CONSTANT
news = 'https://www.9news.com.au/'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# getting HTML file
response = requests.get(news,headers=header)
response.raise_for_status()
contents = response.content

# making soup
soup = BeautifulSoup(contents,'html.parser')
top_news = soup.find_all('h1')
print(f'The main news of today is {top_news[0].text}')
other_news = soup.find_all('h3')
other_news = other_news[:24]
print('Top news in Australia are:')
for i,news in enumerate(other_news,1):
    print(f'{i}. {news.text}')
