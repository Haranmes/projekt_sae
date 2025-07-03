from .medium import Medium
class Zeitschrift(Medium):
    def __init__(self, titel : str, ausgabe: str, erscheinungsjahr: int):
        super().__init__(titel)
        self._ausgabe = ausgabe
        self._erscheinnungsjahr = erscheinungsjahr
        
    def to_dict(self):
        """Gibt ein Dictionary mit sauberen Attributnamen zurück"""
        return {
            'id': self._id,
            'titel': self._titel,
            'ausgabe': self._ausgabe,
            'erscheinungsjahr': self._erscheinnungsjahr,
            'ausgeliehen': self._ausgeliehen
        }
        
        
