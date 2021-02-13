# OC_Scrapper_Project_2

OC_scrapper est un logiciel de Scrapping developé pour le site Book To Scrape 
Il créer un document en format csv pour chaque catégorie 

# Resultats : 
Chaque ficher porte le format : categorie.csv 
Il contient les informations suivantes : 
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

# Constitution :

- __init__.py est l'executable.

- le dossier Classes contient un fichier __init__.py qui contient les classes.
- de même pour le dossier Fonctions qui contient un fichier __init__.py qui contient les fonctions.

- Requirement.txt contient la liste de tous les modules nécessaires au bon fonctionnement.
# Mise en place de l'environement Virturel :

- creation du nouvel environement :

python3 -m venv /path/to/new/virtual/environment

- acceder à l'environement :

sur Windows utiliser :

c:\>c:\Python35\python -m venv c:\path\to\myenv

sur Mac et Linux  utiliser :

c:\>python -m venv c:\path\to\myenv

- instalation des packages :

il vous faudra installer bs4 et request

python3 pip install bs4

python3 pip install request

