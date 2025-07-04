from .medium import Medium


class Zeitschrift(Medium):
    def __init__(self, titel : str, ausgabe: str, erscheinungsjahr: int, ausgeliehen: bool=None, id: int=None):
        super().__init__(titel, ausgeliehen, id)
        self._ausgabe = ausgabe
        self._erscheinungsjahr = erscheinungsjahr


    def to_dict(self) -> dict:
        return {
            'id': self._id,
            'titel': self._titel,
            'ausgabe': self._ausgabe,
            'erscheinungsjahr': self._erscheinungsjahr,
            'ausgeliehen': self._ausgeliehen,
            'typ': self.get_typ()
        }


    def __str__(self) -> str:
        return f"[Zeitschrift {self._id}] | Titel: '{self._titel}', Ausgabe: {self._ausgabe}, Erscheinungsjahr: {self._erscheinungsjahr}"