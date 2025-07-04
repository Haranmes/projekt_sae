from abc import ABC, abstractmethod
import json


from .nutzer import Nutzer


class Medium(ABC):
    id: int = 1


    typen: dict = {
        'BUCH': 0,
        'ZEITSCHRIFT': 1,
        'DIGITALESMEDIUM': 2
    }
    

    def __init__(self, titel: str, ausgeliehen: bool=None, id: int=None):
        self._titel = titel
        self._ausgeliehen = ausgeliehen

        if id is not None:
            self._id = id

            if id > Medium.id:
                Medium.id = id + 1
        else:
            self._id = Medium.id
            Medium.id += 1


    def get_id(self) -> int:
        return self._id


    def get_titel(self) -> str:
        return self._titel


    def get_ausgeliehen(self) -> int:
        return self._ausgeliehen


    def get_typ(self) -> int:
        return Medium.typen.get(self.__class__.__name__.upper())


    def ausleihen(self, nutzer: Nutzer) -> bool:
        if self._ausgeliehen is not None:
            return False
        
        self._ausgeliehen = nutzer.get_id()
        return True


    def zurueckgeben(self) -> bool:
        if self._ausgeliehen is None:
            return False
    
        self._ausgeliehen = None
        return True


    @abstractmethod
    def to_dict() -> dict:
        pass