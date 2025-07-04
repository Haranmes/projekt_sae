from .medium import Medium


class Buch(Medium):
    def __init__(self, titel: str, autor: str, isbn: str, seitenzahl: int, ausgeliehen: bool=None, id: int=None):
        super().__init__(titel, ausgeliehen, id)
        self._autor = autor
        self._isbn = isbn
        self._seitenzahl = seitenzahl
    

    def to_dict(self) -> dict:
        return {
            'id': self._id,
            'titel': self._titel,
            'autor': self._autor,
            'isbn': self._isbn,
            'seitenzahl': self._seitenzahl,
            'ausgeliehen': self._ausgeliehen,
            'typ': self.get_typ()
        }


    def __str__(self) -> str:
        return f"[Buch {self._id}] | Titel: '{self._titel}', Autor: {self._autor}, ISBN: {self._isbn}, Seitenzahl: {self._seitenzahl}"