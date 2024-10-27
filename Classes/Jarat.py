from abc import ABC, abstractmethod


class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar, elerhetoseg):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.elerhetoseg = elerhetoseg

    def __str__(self):
        return f'{self.jaratszam} {self.celallomas} {self.jegyar}'