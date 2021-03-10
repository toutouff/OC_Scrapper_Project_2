import requests
import csv
from bs4 import BeautifulSoup


class Category:
    def __init__(self, name, url):
        self.bookData = []
        self.name = name
        self.url = [url]
        self.books = []
        self.bookLinks = []
        self.response = requests.get(self.url[0])
        self.soup = BeautifulSoup(self.response.text, features="html.parser")

    def get_book_links(self):
        self.get_all_page()
        for url in self.url:
            self.response = requests.get(url)
            self.soup = BeautifulSoup(self.response.text, features="html.parser")
            articles = self.soup.find_all('article', class_="product_pod")
            article_link_start = 'http://books.toscrape.com/catalogue/'
            for article in articles:
                article_a = article.find('a')
                article_link = str(article_a['href'])
                article_link = article_link.replace('../', '')
                self.bookLinks.append(article_link_start + article_link)
        return self.bookLinks

    def add_books(self):
        self.get_book_links()
        for bookLink in self.bookLinks:
            book = Book(bookLink, self.name)
            book.get_info()
            self.bookData.append(book.Info)
            self.books.append(book)

    def get_all_page(self):
        strong = self.soup.findAll('strong')
        nbr_tot_prod = int(strong[1].text)
        i = 2
        while nbr_tot_prod > 20:
            prov_url = self.url[0].replace('index.html', 'page-' + str(i) + '.html')
            self.url.append(prov_url)
            i = i + 1
            nbr_tot_prod = nbr_tot_prod - 20

    def create_csv(self):
        csv_file = self.name + '.csv'
        with open("data/" + csv_file, 'w') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=self.bookData[0].keys())
            writer.writeheader()
            for data in self.bookData:
                writer.writerow(data)


class Book:

    def __init__(self, url, category):
        self.img = ''
        self.url = url
        self.category = category

    def response(self):
        response = requests.get(self.url)
        self.soup = BeautifulSoup(response.text, features='html.parser')
        return response

    def get_title(self):
        title = self.soup.find('h1').text
        self.title = title

    def get_info(self):
        self.response()
        table = self.soup.find('table', class_='table table-striped')
        td = table.findAll('td')
        self.upc = td[0].text
        self.priceeExTax = str(td[2].text)
        self.priceIncTax = str(td[3].text)
        self.nbrAiv = td[5].text
        self.get_title()
        self.get_product_description()
        self.getImg()
        self.getStarRating()
        self.Info = {
            'url': self.url,
            'upc': self.upc,
            'title': self.title,
            'price_including_tax': self.priceIncTax.replace('Â', ''),
            'price_excluding_tax': self.priceeExTax.replace('Â', ''),
            'number_available': self.nbrAiv,
            'product_description': self.product_description,
            'category': self.category,
            'review_rating': self.starRating,
            'image_url': self.img
        }
        return self.Info

    def get_product_description(self):
        all_p = self.soup.findAll('p')
        self.product_description = str(all_p[3].text)

    def getImg(self):
        row = self.soup.find_all('div', class_='col-sm-6')
        img = row[0].find('img')
        img = str(img['src'])
        self.img = 'https://books.toscrape.com/' + img.replace('../', '')
        try:
            self.downLoadImg()
        except:
            print("une erreur est survenue lors du telechargement ")

    def getStarRating(self):
        div = self.soup.findAll('div', class_='col-sm-6')
        p = div[1].findAll('p')
        p = p[2]
        star_rating = str(p['class'])
        self.starRating = str(star_rating)

    def downLoadImg(self):
        img_url = self.img
        response = requests.get(img_url)
        img_title = self.title + ".png"
        img_title = img_title.replace('/', '')
        with open("data/" + img_title, "wb") as img_file:
            img_file.write(response.content)
            img_file.close()
        print(img_title)

