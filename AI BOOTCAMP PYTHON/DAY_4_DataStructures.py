# List
predator = ["Lion", "Tiger", "Crocodile"]

# print(predator) #Ini perintah untuk mencetak list predator
print(predator)

#SLICING LIST
## sliced_predator = predator[1:3]  # Mengambil index 1 dan 2 saja
## print(sliced_predator)  # untuk mengambil data dari list di index
## Outputnya adalah: ['Tiger', 'Crocodile']

## sliced_predator = predator[:3]  # mengambil dari awal sampai index 2
## print(sliced_predator)
## Outputnya adalah: ['Lion', 'Tiger', 'Crocodile']

## sliced_predator = predator[1:]  # mengambil dari index 1 sampai akhir
## print(sliced_predator)
## Outputnya adalah: ['Tiger', 'Crocodile']

predator.append("Puma")  # Ini untuk menambahkan string("Puma") di akhir.
predator.insert(1, "Bear")  # Untuk menambahkan string("Bear") di index 1
print(predator)  # menambahkan Bear dan Puma
# output ['Lion', 'Bear', 'Tiger', 'Crocodile', 'Puma']

predator.remove("Tiger")  # untuk menghapus string "Tiger"
print(predator)  # menghapus Tiger
# output ['Lion', 'Bear', 'Crocodile', 'Puma']

del predator[0]  # fungsinya untuk menghapus index yang ingin di hapus
print(predator)  # menghapus [0] Lion
# output ['Bear', 'Crocodile', 'Puma']

predator.pop()  # menghapus index terakhir yang ada di list predator
print(predator)  # menghapus Puma
# output ['Bear', 'Crocodile']
asasda
#TUPLE
