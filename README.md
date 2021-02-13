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

# Constitution :

- __init__.py est l'executable .

- le dossier Classes contient un fichier __init__.py qui contient les classes.
- de meme pour le dossier Fonctions qui contient un fichier __init__.py qui contient les fonctions.

- Requirement.txt contient la liste de tout les module nécessaire au bon fonctionnement
# Mise en place de l'environement Virtur- reat
python3 -m venv /path/to/new/virtual/environment
