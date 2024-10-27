import itertools
from datetime import datetime

from Classes.LegiTarsasag import LegiTarsasag


class JegyFoglalas:

    id_iter = itertools.count()

    def __init__(self, jarat, indulasi_ido, foglalo_neve):
        self.id = next(self.id_iter)

        print(f"jarat {jarat}")
        #if LegiTarsasag.is_exist(jarat):
        #    pass
        #if not jarat:
        #    print(f"not jarat: {jarat}")
        #    pass
        #if LegiTarsasag.is_exist():
        #    print(f"Létezik a megadott járat: {jarat}")

        if jarat.elerhetoseg == "nem":
            raise Exception("Járat nem elérhető")
        self.jarat = jarat

        timeformat = "%H:%M"
        try:
            datetime.strptime(indulasi_ido, timeformat)
            self.indulasi_ido = indulasi_ido
        except ValueError:
            print(f"{indulasi_ido} is not a valid date")
            self.indulasi_ido = None

        #self.indulasi_ido = indulasi_ido
        self.foglalo_neve = foglalo_neve

    def __str__(self):
        return f"Foglalás{self.id} {self.jarat} járatra {self.indulasi_ido} indulással {self.foglalo_neve} néven. "

    def verify_indulasi_ido(self):
        pass