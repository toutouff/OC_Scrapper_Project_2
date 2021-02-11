# OC_Scrapper_Project_2

OC_scrapper est un logiciel de Scrapping developer pour le site Book To Scrape 
Il créé un document , en format csv , pour chaque catégorie 

# Resultat : 
Chaque ficher porte le format : categorie.csv 
Il contient les information suivante : 
- product_page_url
- universal_ product_code (upc)
- title
- price_including_tax
- price_excluding_tax
- number_available
- product_description
- category
- review_rating
- image_url

La premiere ligne de chaque colonne indique sont contenu 

# Constitution du programe

- main.py est le programme a compiler et executer a l’aide de python 3 

- BookClass.py et CategorieClass.py sont des ficher class qui contienne respectivement les class Book(livre) et Catégorie 

- Requirement.txt contient la liste de tout les module nécessaire au bon fonctionnement
