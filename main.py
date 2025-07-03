import json
from Medienarten import *
from Medienarten.nutzer import Nutzer
def main():
    try:
        
        verwaltung = Verwaltung("MeineBibliothek")

        buch = Buch("Der linux user 4000", "ramez solimannnn", "4232903458", 1000)
        zeitschrift = Zeitschrift("Tim Gotschalk", "12", 2023)
        digitales_medium = DigitalesMedium("eine undendliche geschichte", "CD", "2:00")
        print(buch.__dict__)

        # verwaltung.medium_entfernen(0)
        nutzer1 = Nutzer(1, "Max Mustermann")
        nutzer2 = Nutzer(2, "Erika Musterfrau")

        # verwaltung.ausleihen(2,2)
        # verwaltung.nutzer_hinzufuegen(nutzer2.to_dict())
        users = verwaltung.get_all_users()
        
        num = 0
        for user in users:
            print(users[num].get("name"))
            num += 1
        medien = verwaltung.get_all_medien()
        num = 0
        for medium in medien:
            print(medien[num].get("titel"))
            num += 1
        
    except ValueError as e:
        print(f"Fehler: {e}")
        
        
        
if __name__ == "__main__":
    main()