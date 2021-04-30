class persegi_panjang:
    # variabel biasa
    counter = 0

    # constructor
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l

  # enkapsulasi
    # setter panjang
    # untuk mengubah panjang
    def ubahPanjang(self, p):
        self.panjang = p

    # setter lebar
    # untuk mengubah lebar
    def ubahLebar(self, l):
        self.lebar = l

  #-- akhir enkapsulasi

    def hitungLuas(self):
        return self.panjang * self.lebar

    def hitungKeliling(self):
        return 2 * (self.panjang + self.lebar)

    def cetakLuas(self):
        print('Luas persegi panjang : %d' %self.hitungLuas())

    def cetakKeliling(self):
        print('Keliling persegi panjang : %d' %self.hitungKeliling())

objekPP1 = persegi_panjang(10, 7)
objekPP2 = persegi_panjang(7, 5)
objekPP3 = persegi_panjang(4, 4)

objekPP1.cetakLuas()
objekPP2.cetakKeliling()
objekPP3.counter = 10