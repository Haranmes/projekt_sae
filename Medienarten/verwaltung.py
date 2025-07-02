# importing all classes
from typing import List, Optional
from .buch import Buch
from .zeitschrift import Zeitschrift
from .digitalesMedium import DigitalesMedium
from .nutzer import Nutzer
import re
import os
import json
  

class Verwaltung():
    def __init__(self, name: str):
        self.__name = name
        
        res = re.sub(r'[^a-zA-Z0-9]', '', name)
        if res == '':
            raise ValueError("Der Name darf nicht leer sein und darf nur alphanumerische Zeichen enthalten.")
        
        self.__dateiname = f"verwaltung_{res}.json"
        
        data = self.datei_laden()
        self.__medien = data.get("medien", [])
        self.__nutzer = data.get("nutzer", [])
        
    def datei_laden(self) -> dict:
        data = {}
        
        if os.path.exists(self.__dateiname):
            try:
                with open(self.__dateiname, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    print(data)
            except json.JSONDecodeError:
                print(f"Fehler beim Laden der Datei {self.__dateiname}.")
        
        return data
    
    def datei_speichern(self):
        data = {
            "medien": self.__medien,
            "nutzer": self.__nutzer
        }
        
        try:
            with open(self.__dateiname, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except IOError:
            print(f"Fehler beim Speichern der Datei {self.__dateiname}.")
            
    def nutzer_hinzufuegen(self, nutzer: Nutzer):
        self.__nutzer.append(nutzer)
        self.datei_speichern()
        
    def nutzer_entfernen(self, nutzer_id: str):
        for nutzer in self.__nutzer:
            if nutzer.id == nutzer_id:
                self.__nutzer.remove(nutzer)
                self.datei_speichern()
                
    def medium_hinzufuegen(self, medium: Buch | Zeitschrift | DigitalesMedium):
          if medium not in self.__medien:
            self.__medien.append(medium)
            self.datei_speichern()
        
    def medium_entfernen(self, medium_id: str):
        for medium in self.__medien:
            if medium.get("_id") == medium_id:
                self.__medien.remove(medium)
                self.datei_speichern()
                
    def ausleihen(self, nutzer_id: str, medium_id: str):
        medium = [m for m in self.__medien if m.id == medium_id][0]
        medium.ausleihen(nutzer_id)
        self.datei_speichern()
        
    def zurueckgeben(self, medium_id: str):
        medium = [m for m in self.__medien if m.id == medium_id][0]
        medium.zurueckgeben()
        self.datei_speichern()