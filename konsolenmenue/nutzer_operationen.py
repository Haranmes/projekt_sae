from typing import List, Optional
import questionary

from classes import *


def nutzer_erstellen(verwaltung: Verwaltung):
    name: str = questionary.text("Wie heißt der neue Nutzer?").ask()
    nutzer: Nutzer = Nutzer(name)
    verwaltung.nutzer_hinzufuegen(nutzer)
    print(f"Der Nutzer '{name}' wurde der Verwaltung hinzugefügt")


def nutzer_loeschen(verwaltung: Verwaltung) -> None:
    nutzer: Nutzer = nutzer_auswahl(verwaltung)

    if nutzer is None:
        print("Diese Verwaltung hat keine Nutzer")
        return

    verwaltung.nutzer_entfernen(nutzer)
    print("Der Nutzer wurde gelöscht")


def nutzer_auswahl(verwaltung: Verwaltung) -> Optional[Nutzer]:
    nutzer: List[Nutzer] = verwaltung.get_nutzer()

    if len(nutzer) == 0:
        return None

    wahl: str = questionary.select(
        "Wählen Sie den Nutzer aus:",
        [n.__str__() for n in nutzer]
    ).ask()

    for n in nutzer:
        if wahl == n.__str__():
            return n