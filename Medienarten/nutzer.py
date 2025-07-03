class Nutzer():
    def __init__(self, id: int, name: str):
        self.__id = id
        self.__name = name
        self.__ausgeliehene_medien = []
    def to_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'ausgeliehene_medien': self.__ausgeliehene_medien
        }
    
    