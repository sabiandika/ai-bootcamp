#Numpy is library in python untuk operasi matematika
import numpy as np 

#berfungsi untuk mengubah data menjadi array,output tanpa koms
arrayy = np.array([1, 2, 3, 4, 5])
print(arrayy)

#berfungsi untuk menghasilkan array dengan nilai 0 semua
zeroes =np.zeros((3,3))#dengan urutan 3 kebawah dan 3 kesamping
print(zeroes)

#berfungsi untuk menghasilkan array dengan nilai 1 semua
ones = np.ones((2,3)) #dengan urutan 2 kebawah dan 3 kesamping
print(ones)

#np.arange(start, stop, step)
range_array = np.arange(1, 10, 2) #array NumPy dengan nilai berurutan dari 1 hingga sebelum 10, dengan selisih 2 antar elemen
print(range_array)

#np.linspace(start, stop, num)
linspace_array = np.linspace(0, 10, 5) #membuat array berisi num jumlah angka yang dibagi sama rata dari start sampai stop
print(linspace_array)

print("arr reshape")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
refresh = arr.reshape((2,4)) #contoh array 1 dimensi 
print(refresh)

arr = np.array([1, 2, 3, 4, 5, 6])
expanded = arr[:, np.newaxis] #new axxis menambahkan menambahkan 1 dimensi tambahan di posisi kolo jadi 2 dimensi hasilnya akan kebawah
print(expanded)
print(arr)

a = np.array([1, 2, 3])
b= np.array([4, 5, 6])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

arr = np.array([4, 16, 25])
print(np.sqrt(arr)) #menghitung akar kuadrat dari setiap elemen
print(np.sum(arr)) #menghitung jumlah elemen
print(np.mean(arr)) #menghitung rata-rata elemen
print(np.median(arr)) #menghitung nilai tengah dari elemen
print(np.std(arr)) #menghitung deviasi standar dari elemen
print(np.var(arr)) #menghitung variansi dari elemen
print(np.max(arr)) #menghitung nilai maksimum dari elemen
print(np.min(arr)) #menghitung nilai minimum dari elemen
print(np.sort(arr)) #mengurutkan elemen dari kecil ke besar

print("indeks")
arr = np.array([10, 20, 30, 40, 50])
print(arr[2])  # 0   1   2   3   4   indeks didalam array dimulai dari angka 0
print(arr[-1])
print(arr[1:4])

#HANDS ON EXERCISE
#1. Buatlah array 2D dengan 3 baris dan 4 kolom
print("tugas 1")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr)

transpose = arr.T #mengubah baris menjadi kolom dan kolom menjadi baris
print("Transpose: \n",  transpose)

another_matrix = np.array([[12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]])
print("tambah: \n", arr + another_matrix)
print("kali: \n", arr * another_matrix)
#2. Buatlah array 1D dengan 5 elemen
print("tugas 2")
a = np.arange(1, 6)
b = np.arange(6, 11)
print(a)
print(b)

print("tambah: ", a + b)
print("kali: ",a * b)
print("kurang: ",a - b)
print("bagi: ",a / b)


