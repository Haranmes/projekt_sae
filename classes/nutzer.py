class Nutzer():

    id: int = 1

    def __init__(self, name: str, id: int=None):
        self._name = name

        if id is not None:
            self._id = id

            if id > Nutzer.id:
                Nutzer.id = id + 1
        else:
            self._id = Nutzer.id
            Nutzer.id += 1

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def to_dict(self):
        return {
            'id': self._id,
            'name': self._name
        }

    def __str__(self) -> str:
        return f"[Nutzer {self._id}] | Name: '{self._name}'"