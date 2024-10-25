class FoglalasTarolo:
    def __init__(self):
        self._foglalasok = []

    def add_foglalas(self, foglalas):
        self._foglalasok.append(foglalas)

    def get_foglalasok(self):
        for foglalas in self._foglalasok:
            print(foglalas)