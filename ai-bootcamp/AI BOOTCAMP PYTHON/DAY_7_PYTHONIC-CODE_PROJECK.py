#[EKSPRESI UNTUK ITEM DALAM KONDISI ITERABLE IF]

#BIKIN LIST DARI PERPANGKATAN
squares = [x**2 for x in range(11)] #logikanya x**2 = x akan di pangkat 2, untuk(for) x di(in) jangkauan 11.
print(squares)

#Filter angka genap
pilter = [x for x in range(13) if x % 2 == 0]  #sama seperti yang diatas namun, pada if x akan di bagi dengan dua dan akan print bila sisa bagi x = 0
print(pilter)                   #[x % 2 != 0] jika ingin angka ganjil

#LAMBDA FUNCTION (Fungsi sangat sederhana(tidak diberi nama))
#lambda argumen : expresi (sintaks)

kali = lambda x, y :x * y
print(kali(3,5))


# map()  (Menerapkan fungsi ke setiap item dalam iterable (seperti list), dan mengembalikan hasilnya.)
#map(function, iterable) (sintaks)
numbers = [1, 2, 3, 4]
squares = map(lambda x: x**2, numbers)
print(list(squares))

#filter() (Menyaring item dalam iterable berdasarkan kondisi (True/False) dari fungsi.)
#filter(function, iterable) (sintaks)
angka = [1, 2, 3, 4,]
even = filter(lambda x: x % 2 == 0, angka)
print(list(even))

#reduce() (menggabungkan semua item dalam iterable menjadi satu nilai)
#from functools import reduce
#reduce(function, iterable)   (sintaks)

from functools import reduce

numbers = [1, 2, 3, 4] # 1x2= 2, 2x3= 6, 6x4=24 
product = reduce(lambda x,y: x * y, numbers)
print(product) #ouput 24

#OS DAN SYS MODUL
#os menyediakan fungsi untuk berinteraksi dengan sistem operasi
import os
print(os.getcwd()) #untuk cek direktori saat ini
#os.remove("nama_file") akan menghapus file
#os.mkdir("nama_folder") akan membuat folder

#sys menyediakan akses ke parameter dan fungsi spesifik sistem
import sys
print(sys.platform) #untuk cek sistem operasi yang digunakan.
print(sys.argv[0]) #sys.argv adalah list (daftar) yang berisi argumen command-line. Elemen-elemen berikutnya (sys.argv[1], sys.argv[2], dst.) adalah argumen yang Anda tambahkan saat menjalankan skrip
print(sys.version) #untuk cek versi python yang digunakan. 
