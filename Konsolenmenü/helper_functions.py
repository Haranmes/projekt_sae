import questionary
from Medienarten import *

def nutzer_erstellen(verwaltung : Verwaltung):
    answer = questionary.text("Wie heißt der neue Nutzer?").ask()
    nutzer = Nutzer("1", answer)
    verwaltung.nutzer_hinzufuegen(nutzer)
    print(f"Der Nutzer {nutzer.__name} wurde zur Bibliothek hinzugefügt")

def registrieren_medium(verwaltung : Verwaltung): 
    medium_choice = [
            "Buch",
            "Ein digitales Medium",
            "Eine Zeitschrift"
        ]

    answer = questionary.rawselect(
        "Welches Medium wollen Sie registrieren?",
        medium_choice
    ).ask()

    if answer == ddd
