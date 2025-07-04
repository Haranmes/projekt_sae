from typing import List, Optional
import os
import json
import re

from .medium import Medium
from .buch import Buch
from .zeitschrift import Zeitschrift
from .digitalesMedium import DigitalesMedium
from .nutzer import Nutzer
  

class Verwaltung:
    def __init__(self, name: str):
        self._name = name
        self._dateiname = self._erstelle_dateiname(name)

        self._medien = []
        self._nutzer = []
        self.datei_laden()
    

    def _erstelle_dateiname(self, name: str) -> str:
        res: str = re.sub(r'[^a-zA-Z0-9]', '', name)
        if res == '':
            raise ValueError("Der Name darf nicht leer sein und darf nur alphanumerische Zeichen enthalten.")
        return f"./verwaltungen/verwaltung_{res}.json"


    def datei_laden(self) -> None:
        if not os.path.exists(self._dateiname):
            return
            
        daten: dict = None

        try:
            with open(self._dateiname, 'r', encoding='utf-8') as datei:
                daten = json.load(datei)

        except json.JSONDecodeError:
            print(f"Fehler beim Laden der Datei {self._dateiname}.")
            daten = {}

        for medium in daten.get("medien", []):
            self._medien.append(Verwaltung.erstelle_medium(medium))

        for nutzer in daten.get("nutzer", []):
            self._nutzer.append(Nutzer(
                nutzer.get('name'),
                nutzer.get('id')
            ))


    def datei_speichern(self) -> None:
        daten = {
            "medien": [ m.to_dict() for m in self._medien ],
            "nutzer": [ n.to_dict() for n in self._nutzer ]
        }
        
        try:
            with open(self._dateiname, 'w', encoding='utf-8') as datei:
                json.dump(
                    daten,
                    datei,
                    indent=4,
                    ensure_ascii=False
                )

        except IOError:
            print(f"Fehler beim Speichern der Datei {self._dateiname}.")


    def nutzer_hinzufuegen(self, nutzer: Nutzer) -> None:        
        self._nutzer.append(nutzer)
        self.datei_speichern()


    def nutzer_entfernen(self, nutzer: Nutzer) -> None:
        self._nutzer.remove(nutzer)
        self.datei_speichern()


    def medium_hinzufuegen(self, medium: Medium) -> None:      
        self._medien.append(medium)
        self.datei_speichern()


    def medium_entfernen(self, medium: Medium) -> None:
        self._medien.remove(medium)
        self.datei_speichern()


    def ausleihen(self, nutzer: Nutzer, medium: Medium) -> None:
        if medium.ausleihen(nutzer):
            self.datei_speichern()
        else:
            raise ValueError("Das Medium ist bereits ausgeliehen.")


    def zurueckgeben(self, medium: Medium) -> None:
        if medium.zurueckgeben():
            self.datei_speichern()
        else:
            raise ValueError("Das Medium ist nicht ausgeliehen.")


    def erstelle_medium(daten: dict) -> Medium:
        typ = daten.get('typ')

        if (typ == Medium.typen['BUCH']):
            return Buch(
                daten.get("titel"),
                daten.get("autor"),
                daten.get("isbn"),
                daten.get('seitenzahl'),
                daten.get("ausgeliehen"),
                daten.get('id')
            )

        elif (typ == Medium.typen['ZEITSCHRIFT']):
            return Zeitschrift(
                daten.get('titel'),
                daten.get('ausgabe'),
                daten.get('erscheinungsjahr'),
                daten.get("ausgeliehen"),
                daten.get('id')
            )

        elif (typ == Medium.typen['DIGITALESMEDIUM']):
            return DigitalesMedium(
                daten.get('titel'),
                daten.get('format'),
                daten.get('laufzeit'),
                daten.get("ausgeliehen"),
                daten.get('id')
            )


    def get_nutzer(self) -> List[Nutzer]:
        return self._nutzer


    def get_medien(self) -> List[Medium]:
        return self._medien


    def get_typ_medien(self, typ: int) -> List[Medium]:
        return [ m for m in self._medien if m.get_typ() == typ ]


    def get_verfuegbare_medien(self) -> List[Medium]:
        return [ m for m in self._medien if m.get_ausgeliehen() is None ]


    def get_ausgeliehene_medien(self) -> List[Medium]:
        return [ m for m in self._medien if m.get_ausgeliehen() is not None ]


    def __str__(self) -> str:
        return f"Verwaltung '{self._name}' ({len(self._medien)} Medien, {len(self._nutzer)} Nutzer)"