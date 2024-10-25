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
foglalas1 = JegyFoglalas()
foglalas2 = JegyFoglalas()
foglalas3 = JegyFoglalas()
foglalas4 = JegyFoglalas()
foglalas5 = JegyFoglalas()
foglalas6 = JegyFoglalas()

print(f"-----------------------------")
print(f"Repülőjegy Foglalási Rendszer")
print(f"-----------------------------")

foglalas1.to_string()

foglalasok = FoglalasTarolo()
foglalasok.add_foglalas(foglalas1)

foglalasok.get_foglalasok()