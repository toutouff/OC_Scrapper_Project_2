import requests
from bs4 import BeautifulSoup
from CategorieClass import Category

categories = []
links = []
dict = {}


def getCategories():
    url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    reponse = requests.get(url)
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, features="html.parser")
        divSideCategories = soup.find('div', class_='side_categories')
        ulNavList = divSideCategories.find('ul', class_='nav nav-list')
        ulCategories = ulNavList.find('ul')
        aCategories = ulCategories.findAll('a')
        for categorie in aCategories:
            link = categorie['href']
            link = link.replace('../', '')
            categorie = str(categorie.text)
            categorie = categorie.replace('\n', '')
            categorie = categorie.replace('  ', '')
            dict[categorie] = link


getCategories()
print(dict['Mystery'])
mycategori = Category('Mystery', dict['Mystery'])
print(mycategori.url)
mycategori.addBooks()
theBook = mycategori.books[0]
print(theBook.img)