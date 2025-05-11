# integer_var = 10
# float_var = 10.5
# string_var = "dika"
# list_var = [1, 2, 3, 4, 5]
# tuple_var = (2, 3, 4,)
# dictionary_var = {"name": "dika", "age": 18, "job": "AI Engineer"}
# bool_var = True

# print(integer_var) = 10
# print(float_var) = 10,5
# print(string_var) = dika


# # CONTROL FLOW, 1.Check Condition
# print("Check Condition")
# num = 10
# if num > 0:
#     print("Positif Number:", num)
# elif num == 0:
#     print("Its a zero")
# else:
#     print("Negatif Number:", num)

# # dasar-dasar looping
# print("for")
# for i in range(8):
#     print(i)

# # while loop
# print("while")
# count = 5
# while count > 0:
#     print(count)
#     count -= 1

# # break
# print("break")
# for i in range(9):
#     if i == 7:
#         break  # sistem ngebaca program yang i=7 dan break untuk menghentikan looping
#     print(i)

# # continue
# print("continue")
# for i in range(7):  # looping 0-6
#     if i == 4:
#         continue  # sistem ngebaca program yang i=4 dan melompati i=4
#     print(i)

# print("%")
# for i in range(7):
#     if i % 2 == 0:
#         continue  # sistem melompati 0, 2, 4 dan 6 namun tidak print 7 karna tidak ada modulo 7 dalam range
#     print(i)


# # mengecek bilangan prima
# num = int(input("masukkan angka: "))

# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(f"{num} bukan bilangan prime")
#             break
#     else:
#         print(f"{num} adalah bilangan prime")
# else:
#     print(f"{num} bukan bilangan prime")
# # print("masukkan angka: ", num)  # print angka yang diinputkan

# program for find the largest number in a list using for looop

angka = [31, 5, 73, 39, 9, 6, 37, 4, 5, 95, 62, 0, 97]

largest = angka[0]

for nilai in angka:
    if nilai > largest:
        largest = nilai

print("angka tebesar dalam list adalah: ", largest)
