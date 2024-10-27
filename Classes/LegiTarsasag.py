class LegiTarsasag:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self._jaratok = []

    def add_jarat(self, jarat):
        self._jaratok.append(jarat)

    def get_jaratok(self):
        for jarat in self._jaratok:
            print(jarat)

    def is_exist(self, jarat):
        return jarat in self._jaratok

    #def get_jaratok_szamai(self, ):

    def letezoJarat(self, jaratszam):
        for jarat in self._jaratok:
            if jaratszam == jarat.jaratszam:
                return "igen"
        return "nem"
        #if jaratszam in self._jaratok.:
        #    return "igen"
        #if jarat not in self._jaratok:
        #    return "nem"