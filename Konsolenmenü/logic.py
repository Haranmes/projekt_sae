import questionary
from Medienarten import *
from helper_functions import *

def konsolen_menü(): 
    verwaltung = Verwaltung("MeineBibliothek")

    choice = [
        "Erstellen eines neuen Nutzers und Registrierung in der derzeitigen Verwaltung", 
        "Auswählen eines Nutzers",
        "Ein neues Medium hinzufügen"
        "Ein Mediuzm verleihen"
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
        pass

    elif answer == choice[2]:
        # Ein Medium anlegen   
        registrieren_medium(verwaltung=verwaltung)
        




        

