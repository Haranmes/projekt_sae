from classes.medium import Medium
import json
class Buch(Medium):
    def __init__(self, titel : str, autor: str, isbn: str, seitenzahl: int):
        super().__init__(titel)
        self.__autor = autor
        self.__isbn = isbn
        self.__seitenzahl = seitenzahl
