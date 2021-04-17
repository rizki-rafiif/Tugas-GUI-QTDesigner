# mempelajari cara menggunakan function dalam python

# fungsi global
def kali (a,b):
    c = a*b
    return c
fungsi = kali(11,9)
print(fungsi)

# fungsi global (luar)
def cetakBonus(daftar = []):
    # fungsi lokal (dalam)
    def hitungBonus(gaji):
        if gaji < 5000000:
            bonus = 0.05 * gaji
        elif 5000000<= gaji <7500000:
            bonus = 0.1 * gaji
        else :
            bonus = 0.15 * gaji
        return bonus

    for nama, gaji in daftar :
        b = hitungBonus(gaji)
        print('%s\t: %d, %d' %(nama, gaji, b))

data = [
    ('Bee',4000000),
    ('Milla',6000000),
    ('Lilla',8000000)
    ]

cetakBonus(data)
print('-----------------------------------------\n')

# fungsi lambda
max = lambda a, b : a if a > b else b
print(max(25,20))
print('\n')

same = lambda a: True if a == 25 else False
print (same(20))

