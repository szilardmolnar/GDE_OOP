# This is a sample Python script.
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
foglalas2 = JegyFoglalas(jarat1, "25:00", "Nagy István")
#foglalas3 = JegyFoglalas()
#foglalas4 = JegyFoglalas()
#foglalas5 = JegyFoglalas()
#foglalas6 = JegyFoglalas()

foglalasok = FoglalasTarolo()
foglalasok.add_foglalas(foglalas1)
foglalasok.add_foglalas(foglalas2)

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
            #self._hotel.book_by_room_number(room)
            print(f"megadott jarat: {jaratszam}")
            #if LegiTarsasag.letezoJarat(jaratszam) == "igen":
            if legitarsasag.is_valid_jaratszam(jaratszam):
                print(f"Létező járatszám: {jaratszam}")
            #elif LegiTarsasag.letezoJarat(jarat) == "nem":
                if legitarsasag.is_available_jaratszam(jaratszam):
                    foglalas = JegyFoglalas(legitarsasag.get_jarat_by_jaratszam(jaratszam), "0:0", "Molnár")
                    sikeres_foglalas_szama = foglalasok.add_foglalas(foglalas)
                    print(f"Sikeres foglalás {sikeres_foglalas_szama} számon")
                else:
                    print(f"Nem elérhető járat: {jaratszam}")

            else:
                print(f"Nem létező járatszám: {jaratszam}")

            pass
        elif inputszam == 2:
            foglalas = int(input("Add meg a foglalás számát, amit szeretnél lemondani! "))
            #self._hotel.unbook_by_room_number(room)
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

#while True:


#foglalas1.to_string()




foglalasok.get_foglalasok()
foglalasok.get_foglalasok_jaratszamok()
legitarsasag.get_jarat_szamok()
if legitarsasag.is_valid_jaratszam("LH"):
    print(f"ervenyes")

print(f"jaratok listazasa")
legitarsasag.get_jaratok()
print(legitarsasag.get_jarat_by_jaratszam("LH1675"))