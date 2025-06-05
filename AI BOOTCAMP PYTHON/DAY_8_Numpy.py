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
