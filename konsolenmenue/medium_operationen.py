from typing import List, Optional
import questionary

from classes import *
from .infos import *
from .nutzer_operationen import nutzer_auswahl


def medium_hinzufuegen(verwaltung: Verwaltung) -> None:
    optionen: List[str] = [
            "Buch",
            "Digitales Medium",
            "Zeitschrift"
        ]

    wahl: str = questionary.rawselect(
        "Welches Medium wollen Sie registrieren?",
        optionen
    ).ask()

    infos: dict = None

    if wahl == optionen[0]: # Buch hinzufügen
        infos = buch_infos()
        print(f"Das Buch '{infos["titel"]}' wird hinzugefügt.")

    elif wahl == optionen[1]: # Digitales Medium hinzufügen
        infos = dig_med_infos()
        print(f"Das digitale Medium '{infos["titel"]}' wird hinzugefügt.")

    elif wahl == optionen[2]: # Zeitschrift hinzufügen
        infos = zeitschrift_infos()
        print(f"Die Zeitschrift '{infos["titel"]}' wird hinzugefügt.")

    infos["id"] = None
    infos["ausgeliehen"] = None

    medium: Medium = Verwaltung.erstelle_medium(infos)
    verwaltung.medium_hinzufuegen(medium)


def medium_entfernen(verwaltung: Verwaltung) -> None:
    medium: Medium = medium_auswahl(verwaltung=verwaltung, alle=True)

    if medium is None:
        print("Diese Verwaltung hat keine Medien.")
        return
    
    verwaltung.medium_entfernen(medium)
    print("Das Medium wurde gelöscht.")


def medium_ausleihen(verwaltung: Verwaltung) -> None:
    medium: Medium = medium_auswahl(verwaltung=verwaltung, alle=False, verfuegbar=True)

    if medium is None:
        print("Diese Verwaltung hat keine verfügbaren Medien.")
        return
    
    nutzer: Nutzer = nutzer_auswahl(verwaltung=verwaltung)

    if nutzer is None:
        print("Diese Verwaltung hat keine Nutzer.")
        return
    
    verwaltung.ausleihen(nutzer, medium)
    print(f"Das Medium '{medium.get_titel()}' wurde an '{nutzer.get_name()}' verliehen.")


def medium_zurueckgeben(verwaltung: Verwaltung) -> None:
    medium: Medium = medium_auswahl(verwaltung=verwaltung, alle=False, verfuegbar=False)

    if medium is None:
        print("Diese Verwaltung hat keine verliehenen Medien.")
        return
    
    verwaltung.zurueckgeben(medium)
    print(f"Das Medium '{medium.get_titel()} wurde zurückgegeben.")


def medium_auswahl(verwaltung: Verwaltung, alle: bool, verfuegbar: bool=None) -> Optional[Medium]:
    medien: List[Medium] = None

    if alle:
        medien = verwaltung.get_medien()
    elif verfuegbar:
        medien = verwaltung.get_verfuegbare_medien()
    else:
        medien = verwaltung.get_ausgeliehene_medien()

    if len(medien) == 0:
        return None

    wahl: str = questionary.select(
        "Wählen Sie das Medium aus:",
        [ m.__str__() for m in medien ]
    ).ask()

    for m in medien:
        if wahl == m.__str__():
            return m