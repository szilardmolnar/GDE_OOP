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

    def get_jarat_by_jaratszam(self, jaratszam):
        for jarat in self._jaratok:
            if jaratszam == jarat.jaratszam:
                return jarat

    def get_jarat_szamok(self):
        for jarat in self._jaratok:
            print(jarat.jaratszam)

    def is_available_jaratszam(self, jaratszam):
        jarat = self.get_jarat_by_jaratszam(jaratszam)
        if jarat.elerhetoseg == "igen":
            return True
        else:
            return False

    def is_valid_jaratszam(self, jaratszam):
        for jarat in self._jaratok:
            #print(f" j {jarat.jaratszam} ")
            if jarat.jaratszam == jaratszam:
                return True
        return False

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