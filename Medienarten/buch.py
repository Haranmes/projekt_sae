from .medium import Medium
import json
class Buch(Medium):
    def __init__(self, titel : str, autor: str, isbn: str, seitenzahl: int):
        super().__init__(titel)
        self._autor = autor
        self._isbn = isbn
        self._seitenzahl = seitenzahl
    
    def to_dict(self):
        return {
            'id': self._id,
            'titel': self._titel,
            'autor': self._autor,
            'isbn': self._isbn,
            'seitenzahl': self._seitenzahl,
            'ausgeliehen': self._ausgeliehen
        }
