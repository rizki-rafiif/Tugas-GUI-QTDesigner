from abc import ABCMeta, abstractmethod

# kelas abstract
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

# membuat list kosong
mylist = []

mylist.append(SegiEmpat(6,8).luas())

mylist.append(Segitiga(6,5).luas())

mylist.append(Lingkaran(15).luas())

# cek semua elemen mylist dan memanggil metodeluas dari setiap objek
# yang ada dalam mylist
for obj in mylist:
    if not issubclass(obj.__class__, DuaDimensi):
        raise TypeError('Objek harus turunan dari DuaDimensi')
    if isinstance(obj, SegiEmpat):
        print('Luas Segi empat = ', end='')
    if isinstance(obj, Segitiga):
        print('Luas Segitiga = ', end='')
    else:
        print('Luas Segitiga = ', end='')
    print(obj.luas())