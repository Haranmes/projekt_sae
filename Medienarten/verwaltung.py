# Importing all classes
from typing import List, Optional, Union
from .buch import Buch
from .zeitschrift import Zeitschrift
from .digitalesMedium import DigitalesMedium
from .nutzer import Nutzer
from .medium import Medium
import re
import os
import json
  

class Verwaltung:
    """Verwaltet Medien und Nutzer einer Bibliothek."""
    
    def __init__(self, name: str):
        self.__name = name
        self.__dateiname = self._erstelle_dateiname(name)
        data = self.datei_laden()
        self.__medien = data.get("medien", [])
        self.__nutzer = data.get("nutzer", [])
    
    def _erstelle_dateiname(self, name: str) -> str:
        """Erstellt einen gültigen Dateinamen aus dem Namen."""
        res = re.sub(r'[^a-zA-Z0-9]', '', name)
        if res == '':
            raise ValueError("Der Name darf nicht leer sein und darf nur alphanumerische Zeichen enthalten.")
        return f"verwaltung_{res}.json"
        
    def datei_laden(self) -> dict:
        """Lädt die Daten aus der JSON-Datei."""
        if not os.path.exists(self.__dateiname):
            return {}
            
        try:
            with open(self.__dateiname, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Fehler beim Laden der Datei {self.__dateiname}.")
            return {}
    
    def datei_speichern(self):
        """Speichert die aktuellen Daten in die JSON-Datei."""
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
        """Fügt einen neuen Nutzer hinzu, falls er noch nicht existiert."""
        nutzer_id = nutzer.get("id")
        
        if self._nutzer_existiert(nutzer_id):
            print(f"Nutzer mit ID {nutzer_id} existiert bereits.")
            return
        
        self.__nutzer.append(nutzer)
        self.datei_speichern()

        
    def nutzer_entfernen(self, nutzer_id: int):
        """Entfernt einen Nutzer anhand der ID."""
        nutzer = self._finde_nutzer(nutzer_id)
        if nutzer:
            self.__nutzer.remove(nutzer)
            self.datei_speichern()
        else:
            print(f"Nutzer mit ID {nutzer_id} nicht gefunden.")
                
    def medium_hinzufuegen(self, medium: Union[Buch, Zeitschrift, DigitalesMedium]):
        """Fügt ein neues Medium hinzu, falls es noch nicht existiert."""
        medium_id = medium.get("id")
        
        if self._medium_existiert(medium_id):
            print(f"Medium mit ID {medium_id} existiert bereits.")
            return
        
        self.__medien.append(medium)
        self.datei_speichern()
        
    def medium_entfernen(self, medium_id: int):
        """Entfernt ein Medium anhand der ID."""
        medium = self._finde_medium(medium_id)
        if medium:
            self.__medien.remove(medium)
            self.datei_speichern()
        else:
            print(f"Medium mit ID {medium_id} nicht gefunden.")
                
    def ausleihen(self, nutzer_id: int, medium_id: int):
        """Leiht ein Medium an einen Nutzer aus."""
        # Prüfe ob Medium existiert
        medium_data = self._finde_medium(medium_id)
        if not medium_data:
            raise ValueError("Das Medium existiert nicht.")
        
        # Prüfe ob Nutzer existiert
        nutzer_data = self._finde_nutzer(nutzer_id)
        if not nutzer_data:
            raise ValueError("Der Nutzer existiert nicht.")
        
        # Prüfe ob Medium bereits ausgeliehen ist
        if medium_data.get("ausgeliehen") is not None:
            raise ValueError("Das Medium ist bereits ausgeliehen.")
        
        # Erstelle Medium-Objekt
        medium_objekt = self._erstelle_medium_objekt(medium_data)
        if not medium_objekt:
            raise ValueError("Medium-Typ konnte nicht erkannt werden.")
        
        # Führe Ausleihe durch
        medium_objekt.ausleihen(nutzer_id)
        
        # Aktualisiere Medium-Status
        medium_data["ausgeliehen"] = nutzer_id
        
        # Füge Medium zur Nutzerliste hinzu
        if "ausgeliehene_medien" not in nutzer_data:
            nutzer_data["ausgeliehene_medien"] = []
        
        if medium_id not in nutzer_data["ausgeliehene_medien"]:
            nutzer_data["ausgeliehene_medien"].append(medium_id)
        
        self.datei_speichern()

    def zurueckgeben(self, medium_id: int):
        """Gibt ein ausgeliehenes Medium zurück."""
        # Finde das Medium
        medium_data = self._finde_medium(medium_id)
        if not medium_data:
            raise ValueError("Das Medium existiert nicht.")
        
        # Prüfe ob Medium ausgeliehen ist
        nutzer_id = medium_data.get("ausgeliehen")
        if nutzer_id is None:
            raise ValueError("Das Medium ist nicht ausgeliehen.")
        
        # Erstelle Medium-Objekt
        medium_objekt = self._erstelle_medium_objekt(medium_data)
        if not medium_objekt:
            raise ValueError("Medium-Typ konnte nicht erkannt werden.")
        
        # Führe Rückgabe durch
        medium_objekt.zurueckgeben()
        
        # Aktualisiere Medium-Status
        medium_data["ausgeliehen"] = None
        
        # Entferne Medium aus Nutzerliste
        nutzer_data = self._finde_nutzer(nutzer_id)
        if nutzer_data and "ausgeliehene_medien" in nutzer_data:
            if medium_id in nutzer_data["ausgeliehene_medien"]:
                nutzer_data["ausgeliehene_medien"].remove(medium_id)
        
        self.datei_speichern()
    
    def alle_medien_anzeigen(self) -> List[dict]:
        """Gibt alle Medien zurück."""
        return self.__medien
    
    def alle_nutzer_anzeigen(self) -> List[dict]:
        """Gibt alle Nutzer zurück."""
        return self.__nutzer
    
    def verfuegbare_medien_anzeigen(self) -> List[dict]:
        """Gibt alle verfügbaren (nicht ausgeliehenen) Medien zurück."""
        return [medium for medium in self.__medien if medium.get("ausgeliehen") is None]
    
    def ausgeliehene_medien_anzeigen(self) -> List[dict]:
        """Gibt alle ausgeliehenen Medien zurück."""
        return [medium for medium in self.__medien if medium.get("ausgeliehen") is not None]
    
    def _nutzer_existiert(self, nutzer_id: int) -> bool:
        """Prüft, ob ein Nutzer mit der gegebenen ID bereits existiert."""
        return any(n.get("id") == nutzer_id for n in self.__nutzer)
    
    def _medium_existiert(self, medium_id: int) -> bool:
        """Prüft, ob ein Medium mit der gegebenen ID bereits existiert."""
        return any(m.get("id") == medium_id for m in self.__medien)
    
    def _finde_nutzer(self, nutzer_id: int) -> Optional[dict]:
        """Findet einen Nutzer anhand der ID."""
        for nutzer in self.__nutzer:
            if nutzer.get("id") == nutzer_id:
                return nutzer
        return None
    
    def _finde_medium(self, medium_id: int) -> Optional[dict]:
        """Findet ein Medium anhand der ID."""
        for medium in self.__medien:
            if medium.get("id") == medium_id:
                return medium
        return None
    
    def _erstelle_medium_objekt(self, medium_data: dict) -> Optional[Union[Buch, Zeitschrift, DigitalesMedium]]:
        """Erstellt ein Medium-Objekt aus den Daten."""
        try:
            # Versuche Buch zu erstellen
            if "autor" in medium_data and "isbn" in medium_data:
                return Buch(
                    medium_data.get("titel"), 
                    medium_data.get("autor"), 
                    medium_data.get("isbn"), 
                    medium_data.get("seitenzahl")
                )
        except:
            pass
            
        try:
            # Versuche Zeitschrift zu erstellen
            if "ausgabe" in medium_data and "erscheinungsjahr" in medium_data:
                return Zeitschrift(
                    medium_data.get("titel"), 
                    medium_data.get("ausgabe"), 
                    medium_data.get("erscheinungsjahr")
                )
        except:
            pass
            
        try:
            # Versuche Digitales Medium zu erstellen
            if "format" in medium_data and "laufzeit" in medium_data:
                return DigitalesMedium(
                    medium_data.get("titel"), 
                    medium_data.get("format"), 
                    medium_data.get("laufzeit")
                )
        except:
            pass
            
        return None
    def get_all_users(self):
        """Gibt alle Nutzer zurück."""
        with open(self.__dateiname, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data.get("nutzer", [])
        
    def get_all_medien(self):
        """Gibt alle Medien zurück."""
        with open(self.__dateiname, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data.get("medien", [])
