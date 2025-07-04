from typing import List
import questionary

from classes import *


def buch_infos() -> dict:
    fragen: List[dict]  = [
        {
            "type": "text",
            "name": "titel",
            "message": "Wie lautet der Buchtitel?",
        },
        {
            "type": "text",
            "name": "autor",
            "message": "Wie lautet der Autor des Buchs?",
        },
        {
            "type": "text",
            "name": "isbn",
            "message": "Wie lautet die ISBN-Nummer des Buchs?",
        },
        {
            "type": "text",
            "name": "seitenzahl",
            "message": "Wie viele Seiten hat das Buch?",
        },
    ]

    infos: dict = questionary.prompt(fragen)
    infos["typ"] = Medium.typen["BUCH"]
    
    return infos


def zeitschrift_infos() -> dict:
    fragen: List[dict] = [
        {
            "type": "text",
            "name": "titel",
            "message": "Wie lautet der Titel?",
        },
        {
            "type": "text",
            "name": "ausgabe",
            "message": "Um welche Ausgabe handelt es sich?",
        },
        {
            "type": "text",
            "name": "erscheinungsjahr",
            "message": "In welchem Jahr ist die Zeitschrift erschienen?",
        },
    ]

    infos: dict = questionary.prompt(fragen)
    infos["typ"] = Medium.typen["ZEITSCHRIFT"]
    
    return infos


def dig_med_infos() -> dict:
    fragen: List[dict]  = [
        {
            "type": "text",
            "name": "titel",
            "message": "Wie lautet der Titel?",
        },
        {
            "type": "select",
            "name": "format",
            "message": "Selektiere das Format des digitalen Mediums",
            "choices": [ "CD", "DVD", "Blueray" ],
        },
        {
            "type": "text",
            "name": "laufzeit",
            "message": "Was ist die Laufzeit des digitalen Mediums?",
        },
    ]

    infos: dict = questionary.prompt(fragen)
    infos["typ"] = Medium.typen["DIGITALESMEDIUM"]

    return infos