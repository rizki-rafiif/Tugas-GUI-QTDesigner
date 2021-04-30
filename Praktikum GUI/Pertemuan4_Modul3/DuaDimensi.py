# import library abc
from abc import ABCMeta,abstractmethod

# kelas abstract nya
class DuaDimensi(metaclass=ABCMeta):
    @abstractmethod
    def luas(self):
        pass

class SegiEmpat(DuaDimensi):
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l

    def luas(self):
        return self.panjang * self.lebar

class Segitiga(DuaDimensi):
    def __init__(self,a ,t):
        self.alas = a
        self.tinggi = t

    def luas(self):
        return (self.alas * self.tinggi) / 2

class Lingkaran(DuaDimensi):
    def __init__(self, r):
        self.jari = r

    def luas(self):
        import math
        return math.pi * (self.jari ** 2)

# membuat objek
segitiga = Segitiga(4,5)
segiempat = SegiEmpat(5,6)
lingkaran = Lingkaran(14)

# output luasnya
print(segitiga.luas())
print(segiempat.luas())
print(lingkaran.luas())