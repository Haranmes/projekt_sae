import questionary
from Medienarten import *
from .medien_operationen import *
from .nutzer_operationen import *

def konsolen_menü(): 
    verwaltung = Verwaltung("MeineBibliothek")

    choice = [
        "Registrierung eines Nutzers in der Verwaltung",
        "Löschen eines Nutzers", #TODO
        "Ein neues Medium hinzufügen",
        "Ein Medium verleihen", #TODO
        "Medium wurde wieder zurückgegeben",#TODO
        "Beenden"
    ]

    answer = questionary.rawselect(
        "Wählen Sie eine Option aus:",
        choice
    ).ask()

    if answer == choice[0]:
        # Erstellen Nutzers und Registrieren
        nutzer_erstellen(verwaltung=verwaltung)


    elif answer == choice[1]:
        # Auswählen eines Nutzers
        # Hier muss auf die Implementierung von Issue #20 gewartet werden
        nutzer_löschen(verwaltung=verwaltung)

    elif answer == choice[2]:
        # Ein Medium anlegen  
        medium_operationen(verwaltung=verwaltung, registrieren_oder_löschen=True)
    
    elif answer == choice[5]:
        beenden = True
        return beenden        




        

