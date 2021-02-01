import requests
from bs4 import BeautifulSoup


class Book:

    def __init__(self, url, categorie):
        self.img = ''
        self.url = url
        self.categorie = categorie

    def reponse(self):
        reponse = requests.get(self.url)
        self.soup = BeautifulSoup(reponse.text, features='html.parser')
        return reponse

    def getTitle(self):
        title = self.soup.find('h1').text
        self.title = title

    def getInfo(self):
        self.reponse()
        table = self.soup.find('table', class_='table table-striped')
        td = table.findAll('td')
        self.upc = td[0].text
        self.priceeExTax = td[2].text
        self.priceIncTax = td[3].text
        self.nbrAiv = td[5].text
        self.getTitle()
        self.getProductDescription()
        self.getImg()
        self.getStarRating()
        self.Info = {
            'url': self.url,
            'upc': self.upc,
            'title': self.getTitle,
            'price_including_tax': self.priceIncTax,
            'price_excluding_tax': self.priceeExTax,
            'number_available': self.nbrAiv,
            'product_description': self.productdescription,
            'category': self.categorie,
            'review_rating': self.starRating,
            'image_url': self.img
        }
        return self.Info

    def getProductDescription(self):
        allP = self.soup.findAll('p')
        self.productdescription = allP[3].text

    def getImg(self):
        row = self.soup.find_all('div', class_='col-sm-6')
        img = row[0].find('img')
        img = str(img['src'])
        self.img = 'https://books.toscrape.com/' + img.replace('../', '')

    def getStarRating(self):
        div = self.soup.findAll('div', class_='col-sm-6')
        p = div[1].findAll('p')
        p = p[2]
        starRating = p['class']
        self.starRating = starRating[1]

