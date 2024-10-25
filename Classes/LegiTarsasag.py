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