from typing import List
import os
import json
import questionary

from classes import *
from .medium_operationen import *
from .nutzer_operationen import *


def loop_konsolen_menue() -> None:
    verwaltung: Verwaltung = None

    if not os.path.exists("verwaltungen.json"):
        print("Fehler beim Laden der Verwaltungen")
        return
            
    verwaltungen: List[str] = None

    try:
        with open("verwaltungen.json", 'r', encoding='utf-8') as datei:
            verwaltungen = json.load(datei)

    except json.JSONDecodeError:
        print("Fehler beim Laden der Verwaltungen")
        return

    verwaltung = Verwaltung(
        questionary.rawselect(
            "Wählen Sie die korrekte Verwaltung:",
            verwaltungen
        ).ask()
    )

    print(verwaltung)

    while True:
        optionen: List[str] = [
            "Nutzer registrieren",
            "Nutzer löschen",
            "Medium hinzufügen",
            "Medium löschen",
            "Medium verleihen",
            "Medium zurückgeben",
            "Beenden"
        ]

        wahl: str = questionary.rawselect(
            "Wählen Sie eine Option aus:",
            optionen
        ).ask()

        if wahl == optionen[0]: # Nutzer registrieren
            nutzer_erstellen(verwaltung)

        elif wahl == optionen[1]: # Nutzer löschen
            nutzer_loeschen(verwaltung)

        elif wahl == optionen[2]: # Medium hinzufügen 
            medium_hinzufuegen(verwaltung)

        elif wahl == optionen[3]: # Medium löschen
            medium_entfernen(verwaltung)

        elif wahl == optionen[4]: # Medium verleihen
            medium_ausleihen(verwaltung)
        
        elif wahl == optionen[5]: # Medium zurückgeben
            medium_zurueckgeben(verwaltung)

        elif wahl == optionen[6]: # Beenden
            return