import questionary
from Medienarten import *
from .infos import *

def medium_operationen(verwaltung : Verwaltung, registrieren_oder_löschen : bool): 
    medium_choice = [
            "Buch",
            "Ein digitales Medium",
            "Eine Zeitschrift"
        ]
    if registrieren_oder_löschen:
        question = "Welches Medium wollen Sie registrieren?"
    else:
        question = "Welches Medium wollen Sie löschen?"

    answer = questionary.rawselect(
        question,
        medium_choice
    ).ask()

    if answer == medium_choice[0]:
        # Buch
        infos = buch_infos()
        buch = Buch(
            titel=infos["titel"],
            autor=infos["autor"],
            isbn=infos["isbn"],
            seitenzahl=infos["seitenzahl"]
        )
        verwaltung.medium_hinzufuegen(buch.to_dict())
        print(f'Das Buch "{infos["titel"]}" wurde hinzugefügt.')

    elif answer == medium_choice[1]:
        # Digitales Medium hinzufügen

        infos_dig_med = digitales_medium()
        dig_med = DigitalesMedium(
            titel=infos_dig_med["titel"],
            format=infos_dig_med["format"],
            laufzeit=infos_dig_med["laufzeit"]
        )
        verwaltung.medium_hinzufuegen(dig_med.to_dict())
        print(f'Das Buch "{infos_dig_med["titel"]}" wurde hinzugefügt.')
    elif answer == medium_choice[2]:
        # Zeitschrift

        infos_zeitschrift = zeit_schrift()
        zeitschrifte = Zeitschrift(
            titel=infos_zeitschrift["titel"],
            ausgabe=infos_zeitschrift["ausgabe"],
            erscheinungsjahr=infos_zeitschrift["erscheinungsjahr"]
        )
        verwaltung.medium_hinzufuegen(zeitschrifte.to_dict())
        print(f'Die Zeitschrift "{infos_zeitschrift["titel"]}" wurde hinzugefügt.')

