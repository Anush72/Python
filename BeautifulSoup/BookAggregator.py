# Importing the Libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# URL of the book search
best_book_ever = 'https://www.goodreads.com/list/show/1.Best_Books_Ever'
best_science_fiction = 'https://www.goodreads.com/list/show/19341.Best_Science_Fiction_Books'
best_epic_fantasy_fiction = 'https://www.goodreads.com/list/show/50.The_Best_Epic_Fantasy_fiction_'
best_non_fiction = 'https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century'
mystery_thriller = 'https://www.goodreads.com/list/show/71476.Best_Mystery_Thriller_Books'

list_urls = [best_book_ever,best_science_fiction,best_epic_fantasy_fiction,best_non_fiction,mystery_thriller]
# making function to get html file from request

def get_html(website):
    response = requests.get(website,headers=header)
    response.raise_for_status()
    content = response.content
    # making soup
    soup = BeautifulSoup(content,'html.parser')
    return soup

#making the class to get the list of heading, author, genre and ratings

class Soup(BeautifulSoup):
    def __init__(self,soup):
        self.soup = soup
    # Making function to get the title of book
    def getting_title(self):
        book_titles = self.soup.select('a.bookTitle Span')
        titles = []
        for title in book_titles:
            titles.append(title.text.strip())
        return titles
    # making function to get the author name
    def get_author(self):
        names = self.soup.find_all('span', {'itemprop': 'author'})
        authors= []
        for name in names:
            authors.append(name.text.strip())
        return authors

    # making function to get the ratings
    def get_ratings(self):
        ratings = self.soup.select('span.minirating')
        rating = []
        for i in ratings:
            rating.append(i.text.strip())
        return rating

# Book dictionary to store books details with title,author,reviews and genre
book_dict = {}

#Getting all details of book and storing on dictionary
for i in list_urls:
    html_file = get_html(i)
    html_soup = Soup(html_file)
    title = html_soup.getting_title()
    author = html_soup.get_author()
    reviews = html_soup.get_ratings()
    book_dict['Title'] = title
    book_dict['author'] = author
    book_dict['reviews'] = reviews

# Storing the dictionary in dataframe
book_dataframe = pd.DataFrame(book_dict)

# save to csv
book_dataframe.to_csv('goodreads_books.csv',index=False)