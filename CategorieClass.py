import requests
from bs4 import BeautifulSoup
from BookClass import Book

class Category:
    def __init__(self, name, url):
        self.name = name
        self.url = [url]
        self.books = []
        self.bookLinks = []
        self.reponse = requests.get(self.url[0])
        self.soup = BeautifulSoup(self.reponse.text, features="html.parser")

    def getBookLinks(self):
        self.getAllPage()
        for url in self.url:
            self.reponse = requests.get(url)
            self.soup = BeautifulSoup(self.reponse.text, features="html.parser")
            articles = self.soup.find_all('article', class_="product_pod")
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

    def getAllPage(self):
        strong = self.soup.findAll('strong')
        nbrTotProd = int(strong[1].text)
        i = 2
        while nbrTotProd > 20:
            provUrl = self.url[0].replace('index.html', 'page-' + str(i) + '.html')
            self.url.append(provUrl)
            i = i + 1
            nbrTotProd = nbrTotProd - 20
