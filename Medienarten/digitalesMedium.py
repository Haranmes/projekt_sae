from .medium import Medium

class DigitalesMedium(Medium):
    def __init__(self, titel: str, format: str, laufzeit: str):
        super().__init__(titel)
        self._format = format
        self._laufzeit = laufzeit
    
    def to_dict(self):
        """Gibt ein Dictionary mit sauberen Attributnamen zurück"""
        return {
            'id': self._id,
            'titel': self._titel,
            'format': self._format,
            'laufzeit': self._laufzeit,
            'ausgeliehen': self._ausgeliehen
        }
