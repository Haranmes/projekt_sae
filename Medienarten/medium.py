from abc import ABC, abstractmethod
from .nutzer import Nutzer
import json
class Medium(ABC):
    
    id: int = 0
    
    def __init__(self, titel: str):
        self._id = Medium.id
        Medium.id += 1
        self.__titel = titel
        self.__ausgeliehen = None

    def ausleihen(self, nutzer_id: Nutzer) -> bool:
        if self.__ausgeliehen:
            return False
        
        self.__ausgeliehen = nutzer_id
        return True
        
    def zurueckgeben(self) -> bool:
        if not self.__ausgeliehen:
            return False
    
        self.__ausgeliehen = None
        return True

    def to_json(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)
        
    
