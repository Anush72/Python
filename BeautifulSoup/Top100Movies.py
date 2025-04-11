# importing the Libraries
from bs4 import BeautifulSoup
import requests

# CONSTANT
movie = 'https://www.empireonline.com/movies/features/best-movies-2/'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}


# getting the HTML file
response = requests.get(movie,headers=header)
response.raise_for_status()
content = response.content

# making soup
soup = BeautifulSoup(content,'html.parser')
movies_list = soup.find_all('h2')
movies_list = movies_list[::-1]
# print the text
for movie in movies_list:
    print(movie.text.strip())