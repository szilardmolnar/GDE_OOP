import itertools
from datetime import datetime

class JegyFoglalas:
    id_iter = itertools.count()
    def __init__(self, jarat, indulasi_ido, foglalo_neve):
        self.id = next(self.id_iter)

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

        self.foglalo_neve = foglalo_neve

    def __str__(self):
        return f"Foglalás{self.id} {self.jarat} járatra {self.indulasi_ido} indulással {self.foglalo_neve} néven. "
