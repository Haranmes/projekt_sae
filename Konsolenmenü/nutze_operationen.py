import questionary
from Medienarten import *

def nutzer_erstellen(verwaltung : Verwaltung):
    # TODO: Refactor mit neuen Nutzermethoden

    answer = questionary.text("Wie heißt der neue Nutzer?").ask()
    nutzer = Nutzer(answer)
    verwaltung.nutzer_hinzufuegen(nutzer.to_dict())
    print(f"Der Nutzer {answer} wurde zur Bibliothek hinzugefügt")

def nutzer_auswahl(verwaltung : Verwaltung):
    users = verwaltung.get_all_users()
    
    user_selection = []

    for user in users:
        user_selection.append(user.get("name"))
    
    nutzer_auswählen = questionary.rawselect(
        "Wählen Sie einen Nutzer aus:",
        user_selection
    ).ask()