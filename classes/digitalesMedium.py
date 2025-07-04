from .medium import Medium


class DigitalesMedium(Medium):
    def __init__(self, titel: str, format: str, laufzeit: str, ausgeliehen: bool=None, id: int=None):
        super().__init__(titel, ausgeliehen, id)
        self._format = format
        self._laufzeit = laufzeit
    

    def to_dict(self) -> dict:
        return {
            'id': self._id,
            'titel': self._titel,
            'format': self._format,
            'laufzeit': self._laufzeit,
            'ausgeliehen': self._ausgeliehen,
            'typ': self.get_typ()
        }


    def __str__(self) -> str:
        return f"[Digitales Medium {self._id}] | Titel: '{self._titel}', Format: {self._format}, Laufzeit: {self._laufzeit}"