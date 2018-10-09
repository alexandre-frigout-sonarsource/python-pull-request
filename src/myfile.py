class Personnage:
    def __init__(self, _age):
        self.age = _age

    def older(self, year):
        self.age += year;
