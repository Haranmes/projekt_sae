class Nutzer():

    id : int = 0

    def __init__(self, name: str):
        Nutzer.id += 1
        self.__id = Nutzer.id  
        self.__name = name

    
    def to_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
        }
    
    