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
        verwaltung.medium_hinzufuegen(buch.to_dict())
        verwaltung.medium_hinzufuegen(zeitschrift.to_dict())
        verwaltung.medium_hinzufuegen(digitales_medium.to_dict())

        # verwaltung.medium_entfernen(0)
        nutzer1 = Nutzer(1, "Max Mustermann")
        nutzer2 = Nutzer(2, "Erika Musterfrau")

        verwaltung.zurueckgeben(0)
        # verwaltung.nutzer_hinzufuegen(nutzer1.to_dict())
     
        
    except ValueError as e:
        print(f"Fehler: {e}")
        
        
        
if __name__ == "__main__":
    main()