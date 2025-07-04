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
        user_selection.append(f"{user.get("id")}")
    
    nutzer_id = questionary.rawselect(
        "Wählen Sie einen Nutzer aus:",
        user_selection
    ).ask()

    choices = [
        "Nutzer löschen",
        "Medium erhalten",
        "Medium verleihen"
    ]
    
    operation = questionary.rawselect(
        f"Nutzeraktion für **{nutzer_name}** auswählen:",
        choices
    )

    

# def nutzer_löschen(nutzer_name : str):

