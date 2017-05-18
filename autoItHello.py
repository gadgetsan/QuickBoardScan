import autoit #pip install -U pyautoit
import easygui #pip install -U easygui
from tinydb import TinyDB, Query #pip install -U tonydb
from datetime import datetime
'''
#AutoIt Hello World
autoit.run("notepad.exe")
autoit.win_wait_active("[CLASS:Notepad]", 3)
autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
'''

'''
#EasyGui Hello World
value = easygui.enterbox()
print(value)

'''
'''
#TinyDB Hello World
db = TinyDB('db.json')
items = db.table('items')
items.insert({'value': 'Scale'})
'''

db = TinyDB('db.json')
items = db.table('items')
data = db.table('data')

def addItem():
    newItemName = easygui.enterbox("Ajouter une le nom de l'item à ajouter (assurez-vous qu'il est bien écrit)", "Ajout d'un item", "")
    #On va valider que l'item n'existe pas deja
    Item = Query()
    searchResult = items.search(Item.name == newItemName)
    if len(searchResult) == 0 :
        items.insert({'name': newItemName})
    else:
       easygui.msgbox("Cet item (" + newItemName + ") est déjà présent")

def listItems():
    allItems = items.all()
    itemListToDisplay = []
    for oneItem in allItems:
        itemListToDisplay.append(oneItem["name"])
    listChoice = easygui.choicebox("Liste des Items - Choisissez un item pour le supprimer", "Liste des Items", itemListToDisplay)
    if listChoice != "" :
        Item = Query()
        items.remove(Item.name == listChoice)

def fetchItemsData():
    allItems = items.all()
    for singleItem in allItems:
        #ici on entrera les touches pour faire la recherche de l'item et afficher son prix de vente
        itemPrice = easygui.enterbox("Entrez le prix le plus bas pour la vente de '" + singleItem["name"] + "'", "Entrée du prix", "")
        data.insert({'name': singleItem["name"], 'price': itemPrice, 'timestamp': str(datetime.now())})



menuChoice=["1 - Ajouter un item à suivre", "2 - Afficher la liste des items à suivre", "3 - Effectuer le suivi des items"]
choice = easygui.choicebox("Que voulez-vous faire?", "Logiciel Awesome", menuChoice)

choiceNum = choice[:1]
print "Choix: " + choice

if int(choiceNum) == 1:
    print "Ajout d'un item"
    addItem()
elif int(choiceNum) == 2:
    print "Liste des items"
    listItems()
elif int(choiceNum) == 3:
    print "Suivi des items"
    fetchItemsData()
else:
    print "Aucun Choix"
