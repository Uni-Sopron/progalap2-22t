
class CharacterModel:
    def __init__(self, name) -> None:
        self.name = name
        self.stats = {
            'STR': 1,
            'INT': 1,
            'DEX': 1
        }

    def getstat(self, statname) -> int:
        return self.stats[statname]

    def setstat(self, statname, value):
        self.stats[statname] = value
