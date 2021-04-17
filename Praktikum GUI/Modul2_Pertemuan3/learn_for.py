# mempelajari for dalam bahasa python
angka = 10

# looping dengan parameter 1 (Max)
for i in range (angka) :
    print('Angka ke : %d' %(i+1))
print('\n')

# looping dengan 2 parameter (min, max) increment
for i in range (angka, 20):
    print('Angka ke : %d' %(i+1))
print('\n')

# looping dengan 3 parameter (min, max, lompatan - decre)
# looping dengan 3 parameter (min, max, lompatan + incre)
for i in range (angka, 1, -1):
    print('Angka ke : %d' %(i+1))
print('\n')

# Array
array = [1,2,3,4,5]

for i in array :
    print(i, end = ' ')
