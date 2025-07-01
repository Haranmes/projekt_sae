import json
from Medienarten.medium import Medium
from Medienarten.buch import Buch
from Medienarten.zeitschrift import Zeitschrift
from Medienarten.digitalesMedium import DigitalesMedium
from Medienarten.nutzer import Nutzer
from Medienarten.verwaltung import Verwaltung

def main():
    try:
        
        verwaltung = Verwaltung("MeineBibliothek")

        buch = Buch("Der linux user 4000", "ramez solimannnn", "4232903458", 1000)
        zeitschrift = Zeitschrift("Tim Gotschalk", "12", 2023)
        digitales_medium = DigitalesMedium("eine undendliche geschichte", "CD", "2:00")

        verwaltung.medium_hinzufuegen(buch.to_json())
        verwaltung.medium_hinzufuegen(zeitschrift.to_json())
        verwaltung.medium_hinzufuegen(digitales_medium.to_json())

        nutzer = Nutzer("1", "Max Mustermann")
        
        verwaltung.nutzer_hinzufuegen(nutzer)
        verwaltung.ausleihen("1", "1")
        
    except ValueError as e:
        print(f"Fehler: {e}")
        
        
        
if __name__ == "__main__":
    main()