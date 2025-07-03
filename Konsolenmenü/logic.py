import questionary
from Medienarten import *
from .medien_operationen import *
from .nutze_operationen import *

def konsolen_menü(): 
    verwaltung = Verwaltung("MeineBibliothek")

    choice = [
        "Erstellen eines neuen Nutzers und Registrierung in der derzeitigen Verwaltung", 
        "Auswählen eines Nutzers",
        "Ein neues Medium hinzufügen"
        "Ein Mediuzm verleihen"
        "Medium wurde wieder zurückgegeben",
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
        nutzer_auswahl(verwaltung=verwaltung)

    elif answer == choice[2]:
        # Ein Medium anlegen  
        medium_operationen(verwaltung=verwaltung, registrieren_oder_löschen=True)
    
    elif answer == choice[3]:
        beenden = True
        return beenden        




        

