
class Controller:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

    def getstat(self) -> int:
        return self.model.getstat()

    def setstat(self, statname, value):
        self.model.setstat(statname, value)
        self.view.update(statname, value)