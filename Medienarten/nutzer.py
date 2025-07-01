import pydantic

class Nutzer(pydantic.BaseModel):
    def __init__(self, id: str, name: str):
        self.__id = id
        self.__name = name
        self.__ausgeliehene_medien = []
    
    