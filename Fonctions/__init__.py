import requests
from bs4 import BeautifulSoup



def main():
    import Classes
    data = get_categories()
    for category in data.keys():
        my_category = Classes.Category(category, data[category])
        my_category.add_books()
        my_category.create_csv()


categories = []
links = []
category_links_dict = {}


def get_categories():
    url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, features="html.parser")
        div_side_categories = soup.find('div', class_='side_categories')
        ul_nav_list = div_side_categories.find('ul', class_='nav nav-list')
        ul_categories = ul_nav_list.find('ul')
        a_categories = ul_categories.findAll('a')
        for category in a_categories:
            link = category['href']
            link = link.replace('../', '')
            category = str(category.text)
            category = category.replace('\n', '')
            category = category.replace('  ', '')
            link = 'http://books.toscrape.com/catalogue/category/' + link
            category_links_dict[category] = link
        return category_links_dict

