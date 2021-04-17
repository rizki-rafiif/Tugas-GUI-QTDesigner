# mempelajari cara menggunakan kelas pada bahasa python

# parameter untuk inheritance
class Titik(object):
    # constructor
    def __init__(self, x = 0, y = 0):
        # self itu sama dengan this kalau di java
        # cuma kalo di python self juga perlu dideklarasikan
        # terlebih dahulu
        self.x = x
        self.y = y

    def pindah(self,x,y):
        self.x = x
        self.y = y

    def cetak(self):
        print(f'{self.x}, {self.y}')


# membuat objek kelas
titik = Titik()
titik.cetak()
titik.pindah(5,10)
titik.cetak()
