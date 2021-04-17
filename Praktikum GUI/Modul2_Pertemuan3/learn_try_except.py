# mempelajari cara menggunakan try dan except dalam bahasa python

# try except dalam pembagian dengan nilai 0
try :
  a = int(input('masukkan nilai a: '))
  b = int(input('masukkan nilai b: '))
  c = a / b
  print("%d / %d = %d" %(a, b, c))

except ZeroDivisionError as e :
  print('Error : Tidak boleh bagi 0')
print('\n')


# try except finally dalam membuka file
f = ''

try : 
  f = open('contoh.txt', 'r')
  lines = f.readlines()
  for line in lines : 
    print(line, end='\n')

except IOError as e :
  print('Error : File Hilang')

finally :
  if f :
    f.close()
