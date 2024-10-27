# This is a sample Python script.
from datetime import datetime

from Classes.FoglalasTarolo import FoglalasTarolo
from Classes.JegyFoglalas import JegyFoglalas
from Classes.LegiTarsasag import LegiTarsasag
from Classes.NemzetkoziJarat import NemzetkoziJarat


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import this



legitarsasag = LegiTarsasag(1, "Lufthansa")
jarat1 = NemzetkoziJarat("LH1335", "Frankfurt am Main", 61259, "igen")
jarat2 = NemzetkoziJarat("LH1343", "Salzburg", 173300, "igen")
jarat3 = NemzetkoziJarat("LH1675", "Copenhagen", 94900, "nem")
legitarsasag.add_jarat(jarat1)
legitarsasag.add_jarat(jarat2)
legitarsasag.add_jarat(jarat3)

foglalas1 = JegyFoglalas(jarat1, "6:45", "Kiss József")
foglalas2 = JegyFoglalas(jarat1, "23:00", "Nagy István")
foglalas3 = JegyFoglalas(jarat2, "10:00", "Kovács László")
foglalas4 = JegyFoglalas(jarat2, "12:30", "Molnár Péter")
foglalas5 = JegyFoglalas(jarat2, "16:45", "Takács Béla")
foglalas6 = JegyFoglalas(jarat2, "17:15", "Tavaszi Virág")

foglalasok = FoglalasTarolo()
foglalasok.add_foglalas(foglalas1)
foglalasok.add_foglalas(foglalas2)
foglalasok.add_foglalas(foglalas3)
foglalasok.add_foglalas(foglalas4)
foglalasok.add_foglalas(foglalas5)
foglalasok.add_foglalas(foglalas6)

print(f"-----------------------------")
print(f"Repülőjegy Foglalási Rendszer")
print(f"-----------------------------")
print(f"FŐMENÜ")
print(f" 1.) Jegy foglalása")
print(f" 2.) Foglalás lemondása")
print(f" 3.) Foglalások listázása")
print(f" 0.) Kilépés")
while True:
    try:
        inputszam = int(input("Add meg a menüpont számát: "))
        if inputszam == 1:
            jaratszam = input("Add meg a járat számát, amire szeretnél helyet foglalni! ")
            if legitarsasag.is_valid_jaratszam(jaratszam):
                if legitarsasag.is_available_jaratszam(jaratszam):
                    while True:
                        try:
                            idopont = input("Add meg az indulás időpontját ! ")
                            timeformat = "%H:%M"
                            datetime.strptime(idopont, timeformat)
                            break
                        except ValueError:
                            print(f"Megadott időpont {idopont} nem érvényes")
                    while True:
                        try:
                            nev = input("Add meg a foglaló nevét: ")
                            if not nev.isalpha():
                                raise ValueError("Csak szöveges bemenetet lehet megadni!")
                            break
                        except ValueError as e:
                            print(e)

                    foglalas = JegyFoglalas(legitarsasag.get_jarat_by_jaratszam(jaratszam), idopont, nev)
                    sikeres_foglalas_szama = foglalasok.add_foglalas(foglalas)
                    print(f"Sikeres foglalás {sikeres_foglalas_szama} számon")
                    print(f"Foglalás ára: {legitarsasag.get_jegyar_by_jaratszam(jaratszam)}Ft ")
                else:
                    print(f"Nem elérhető járat: {jaratszam}")
            else:
                print(f"Nem létező járatszám: {jaratszam}")
            pass
        elif inputszam == 2:
            foglalas = int(input("Add meg a foglalás számát, amit szeretnél lemondani! "))
            torolt_foglalas = foglalasok.remove_foglalas_by_id(foglalas)
            print(f" {torolt_foglalas} számú foglalás törölve ")
            pass
        elif inputszam == 3:
            if foglalasok.get_foglalasok_szama() == 0:
                print(f"Foglalások listája üres")
            foglalasok.get_foglalasok()
            pass
        elif inputszam == 0:
            print(f">>>Kilépés ...")
            break
        print(f"FŐMENÜ: 1.) Jegy foglalása 2.) Foglalás lemondása 3.) Foglalások listázása 0.) Kilépés ")
    except ValueError:
        print("Nem szám típusú, amit beírtál")
