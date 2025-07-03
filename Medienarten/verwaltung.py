# importing all classes
from typing import List, Optional
from .buch import Buch
from .zeitschrift import Zeitschrift
from .digitalesMedium import DigitalesMedium
from .nutzer import Nutzer
from .medium import Medium
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
        if os.path.exists(self.__dateiname) == True:
            with open(self.__dateiname, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if "nutzer" not in data:
                    data["nutzer"] = []
                for n in data["nutzer"]:
                    if n.get("id") == nutzer.get("id"):
                        print(f"Nutzer mit ID {nutzer.get('id')} existiert bereits.")
                        return
                
                data["nutzer"].append(nutzer)
                self.__nutzer = data["nutzer"]
                self.datei_speichern()
        else:
            if nutzer not in self.__nutzer:
                self.__nutzer.append(nutzer)
                self.datei_speichern()

        
    def nutzer_entfernen(self, nutzer_id: int):
        for nutzer in self.__nutzer:
            if nutzer.get("id") == nutzer_id:
                self.__nutzer.remove(nutzer)
                self.datei_speichern()
                
    def medium_hinzufuegen(self, medium: Buch | Zeitschrift | DigitalesMedium):
        if os.path.exists(self.__dateiname) == True:
            with open(self.__dateiname, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if "medien" not in data:
                    data["medien"] = []
                

                for m in data["medien"]:
                    if m.get("id") == medium.get("id"):
                        print(f"Medium mit ID {medium.get('id')} existiert bereits.")
                        return
                

                data["medien"].append(medium)
                self.__medien = data["medien"]
                self.datei_speichern()
        else:
          if medium not in self.__medien:
            self.__medien.append(medium)
            self.datei_speichern()
        
    def medium_entfernen(self, medium_id: int):
        for medium in self.__medien:
            if medium.get("id") == medium_id:
                self.__medien.remove(medium)
                self.datei_speichern()
                
    def ausleihen(self, nutzer_id: int, medium_id: int):
        medium = [m for m in self.__medien if m.get("id") == medium_id][0]
        with open(self.__dateiname, 'r', encoding='utf-8') as file:
            data = json.load(file)
            items = 0

            for id in data.get("medien",{}):
                test = data.get("medien",{})[items]
                if test.get("id") == medium_id:
                    try:
                        medium = Buch(test.get("titel"), test.get("autor"), 
                                    test.get("isbn"), test.get("seitenzahl"))
                        continue
                    except:
                        try:
                            medium = Zeitschrift(test.get("titel"), test.get("ausgabe"), 
                                                    test.get("erscheinungsjahr"))
                            continue
                        except:
                            try:
                                medium = DigitalesMedium(test.get("titel"), test.get("format"), 
                                                    test.get("laufzeit"))
                                continue
                            except:
                                medium = None
                                continue
                            

            
                items += 1

            if medium is not None:
                if data.get("medien",{})[items].get("ausgeliehen") is None:
                    medium.ausleihen(nutzer_id)
                    if medium_id not in self.__nutzer[0]["ausgeliehene_medien"]:
                        nutzer = 0
                        for n in self.__nutzer:
                            if n.get("id") == nutzer_id:
                                self.__nutzer[nutzer]["ausgeliehene_medien"].append(medium_id)
                            nutzer += 1
                    for m in self.__medien:
                        if m.get("id") == medium_id:
                            m["ausgeliehen"] = nutzer_id
                    self.datei_speichern()
                else:
                    raise ValueError("Das Medium ist bereits ausgeliehen.")

    def zurueckgeben(self, medium_id: int):
        medium = [m for m in self.__medien if m.get("id") == medium_id][0]
        with open(self.__dateiname, 'r', encoding='utf-8') as file:
            data = json.load(file)
            items = 0

            for id in data.get("medien",{}):
                test = data.get("medien",{})[items]
                if test.get("id") == medium_id:
                    try:
                        medium = Buch(test.get("titel"), test.get("autor"), 
                                    test.get("isbn"), test.get("seitenzahl"))
                        continue
                    except:
                        try:
                            medium = Zeitschrift(test.get("titel"), test.get("ausgabe"), 
                                                    test.get("erscheinungsjahr"))
                            continue
                        except:
                            try:
                                medium = DigitalesMedium(test.get("titel"), test.get("format"), 
                                                    test.get("laufzeit"))
                                continue
                            except:
                                medium = None
                                continue
                            

            
                items += 1
        if medium is not None:

            nutzer_id = None
            for m in self.__medien:
                if m.get("id") == medium_id:
                    nutzer_id = m.get("ausgeliehen")
                    m["ausgeliehen"] = None  
                    break
            if nutzer_id is not None:
                for n in self.__nutzer:
                    if n.get("id") == nutzer_id and "ausgeliehene_medien" in n:
                        if medium_id in n["ausgeliehene_medien"]:
                            n["ausgeliehene_medien"].remove(medium_id)
                        break
                medium.zurueckgeben()
                self.datei_speichern()
            else:
                raise ValueError("Das Medium ist nicht ausgeliehen.")
        else:
            raise ValueError("Das Medium existiert nicht.")