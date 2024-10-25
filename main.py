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
jarat1 = NemzetkoziJarat("LH1335", "Frankfurt am Main", 61259)
jarat2 = NemzetkoziJarat("LH1343", "Salzburg", 173300)
jarat3 = NemzetkoziJarat("LH1675", "Copenhagen", 94900)

legitarsasag.add_jarat(jarat1)
legitarsasag.add_jarat(jarat2)
legitarsasag.add_jarat(jarat3)

foglalas1 = JegyFoglalas(jarat1, "6:45", "Kiss József")
#foglalas2 = JegyFoglalas()
#foglalas3 = JegyFoglalas()
#foglalas4 = JegyFoglalas()
#foglalas5 = JegyFoglalas()
#foglalas6 = JegyFoglalas()

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
        if inputszam == 0:
            print(f">>>Kilépés ...")
            break
    except ValueError:
        print("Nem szám")

#while True:


foglalas1.to_string()

foglalasok = FoglalasTarolo()
foglalasok.add_foglalas(foglalas1)

foglalasok.get_foglalasok()