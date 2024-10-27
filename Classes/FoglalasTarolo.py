class FoglalasTarolo:
    def __init__(self):
        self._foglalasok = []

    def add_foglalas(self, foglalas):
        self._foglalasok.append(foglalas)
        return foglalas.id

    def remove_foglalas_by_id(self, foglalas_id):
        for foglalas in self._foglalasok:
            if foglalas.id == foglalas_id:
                self._foglalasok.remove(foglalas)
                return foglalas_id

    def get_foglalasok(self):
        for foglalas in self._foglalasok:
            print(foglalas)

    def get_foglalasok_szama(self):
        return len(self._foglalasok)
