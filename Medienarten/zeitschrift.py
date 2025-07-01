from classes.medium import Medium
class Zeitschrift(Medium):
    def __init__(self, titel : str, ausgabe: str, erscheinungsjahr: int):
        super().__init__(titel)
        self.__ausgabe = ausgabe
        self.__erscheinnungsjahr = erscheinungsjahr
        
        
