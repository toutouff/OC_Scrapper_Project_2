import Classes
import Fonctions

data = Fonctions.getCategories()

for categorie in data.keys():
    mycategori = Classes.Category(categorie, data[categorie])
    mycategori.addBooks()
    mycategori.createCsv()


