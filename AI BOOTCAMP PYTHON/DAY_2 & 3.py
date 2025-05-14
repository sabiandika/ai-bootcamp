import math as m
print("DAY 2")
# #SYNTAX FOR-LOOP
# for item in sequence:

print("Contoh for loop memakai list")
zoo = ["lion", "tiger", "bear"]
for animal in zoo:
    print(animal)

print("Contoh loop menggunakan range")
for a in range(8):
    print(a)

# #SYNTAX WHILE-LOOP
# while condition:

print("Contoh menggunakan while loop")
angka = 6
while angka > 0:
    angka -= 1
    print(angka)


print("DAY 3")

print("penggunaan def")
# def nama_fungsi(parameter1, parameter2, ...):
# kode yang dijalankan
# return hasil


# CONTOH PENGGUNAAN DEF
def sapa(nama):
    print(f"Halo", {nama})


sapa("budi")  # output : Halo budi

# syntax def
# def functionn_name(parameter):
# code to be executed
# return result


# print("example")
# # function with parameters and return value


# def add_numbers(a, b):
#     return a + b


# result = add_numbers(21, 5)
# print("Hasilnya adalah: ", result)


# PERBEDAAN LOCAL SCOPE DAN GLOBAL SCOPE

# local scope Variabel yang didefinisikan di dalam fungsi hanya bisa diakses di dalam fungsi itu saja.
def salam():
    pesan = "Halo!"  # ini local scope
    print(pesan)


salam()  # outputnya Halo
# print(pesan)  ❌ Error: 'pesan' tidak bisa diakses di luar fungsi

# global scope Variabel yang didefinisikan di luar semua fungsi bisa diakses di mana saja dalam file tersebut (termasuk di dalam fungsi)
pesan = "Selamat pagi"  # global scope


def cetak():
    print(pesan)  # bisa akses variabel global


cetak()  # outputnya adalah selamat pagi

# modules


# program fakotrial

def factorial(n):
    if n == 0 or n == 1:  # dibuat seprti ini karena faktorial 0 dan 1 adalah 1 dan menggunakan fungsi or
        return 1  # fungsi return 1, sesuai pada perintah di atas jika n 0/1 program akan mengembalikan nilai 1  karena 0!=1, 1!=1
    else:
        # nilai n dikali dengan faktorial, selanjutnya nilai n-1 lalu dikali lagi dengan faktorial, lalu terus melooping sampai n habis
        return n * factorial(n - 1)


# kode ini menggunakan local scope karena variabel disini berada didalam scope
def print_factorial(n):
    # untuk mempermudah pemanggilan dibuatlah variabel result
    result = factorial(n)
    print(f"The faktorial for {n} is {result}")


print_factorial(6)  # pemanggilan fungsi dan menghitung output


# import math_operations as mo
# import diatas bisa digunakan ketika kita membuat file yang sudah berisi fungsi seperti penghitungan lalu beri nama file dan kalian bisa mengimportnya
# num1 = 10
# num2 = 5

# print("Tambah", mo.add(num1, num2))
