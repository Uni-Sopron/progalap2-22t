class Base:
    def __priv(self):
        print("secret")
        
class Child(Base):
    def __init__(self) -> None:
        super().__init__()
        
    def __priv(self):
        print("top secret")

c = Child()
c.__priv()