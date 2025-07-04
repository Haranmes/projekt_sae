import questionary
import logging

def buch_infos():
    questions = [
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

    answers = questionary.prompt(questions)
    return answers

def digitales_medium():
    questions = [
        {
            "type": "text",
            "name": "titel",
            "message": "Wie lautet der Titel?",
        },
        {
            "type": "select",
            "name": "format",
            "message": "Selektiere das Format des digitalen Mediums",
            "choices": ["CD", "DVD", "Blueray"],
        },
        {
            "type": "text",
            "name": "laufzeit",
            "message": "Was ist die Laufzeit des digitalen Mediums?",
        },
    ]

    answers = questionary.prompt(questions)
    return answers

def get_valid_year():
    while True:
        eingabe = questionary.text("Wann ist die Zeitschrift erschienen? (Jahr)").ask()
        try:
            return int(eingabe)
        except ValueError:
            logging.error("Bitte gib eine gültige Jahreszahl ein (z.B. 2023).")

def zeit_schrift():
    titel = questionary.text("Wie lautet der Titel der Zeitschrift?").ask()
    ausgabe = questionary.text("Um welche Ausgabe handelt es sich?").ask()
    erscheinungsjahr = get_valid_year()
    
    return {
        "titel": titel,
        "ausgabe": ausgabe,
        "erscheinungsjahr": erscheinungsjahr,
    }