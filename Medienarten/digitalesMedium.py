from classes.medium import Medium

class DigitalesMedium(Medium):
    def __init__(self, titel: str, format: str, laufzeit: str):
        super().__init__(titel)
        self.__format = format
        self.__laufzeit = laufzeit
