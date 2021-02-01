import requests
from bs4 import BeautifulSoup
from BookClass import Book

class Category:
    def __init__(self, name, url):
        self.name = name
        self.url = 'http://books.toscrape.com/catalogue/category/' + url
        self.books = []
        self.bookLinks = []

    def getBookLinks(self):
        reponse = requests.get(self.url)
        soup = BeautifulSoup(reponse.text, features="html.parser")
        articles = soup.find_all('article', class_="product_pod")
        articleLinkStart = 'http://books.toscrape.com/catalogue/'
        for article in articles:
            articleA = article.find('a')
            articleLink = str(articleA['href'])
            articleLink = articleLink.replace('../', '')
            self.bookLinks.append(articleLinkStart + articleLink)
        return self.bookLinks

    def addBooks(self):
        self.getBookLinks()
        for bookLink in self.bookLinks:
            mybook = Book(bookLink, self.name)
            mybook.getInfo()
            self.books.append(mybook)