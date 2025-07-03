import questionary

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

def zeit_schrift():

    questions = [
        {
            "type": "text",
            "name": "titel",
            "message": "Wie lautet der Titel der Zeitschrift?",
        },
        {
            "type": "text",
            "name": "ausgabe",
            "message": "Um welche Ausgabe handelt es sich?",
        },
        {
            "type": "text",
            "name": "ercheinungsjahr",
            "message": "Wann ist die Zeitschrift erschienen?",
        },
    ]

    answers = questionary.prompt(questions)
    return answers