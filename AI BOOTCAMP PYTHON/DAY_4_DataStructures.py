# List
predator = ["Lion", "Tiger", "Crocodile"]

# print(predator) #Ini perintah untuk mencetak list predator
print(predator)

#SLICING LIST
sliced_predator = predator[1:3]  # Mengambil index 1 dan 2 saja
print(sliced_predator)  # untuk mengambil data dari list di index
#Outputnya adalah: ['Tiger', 'Crocodile']

sliced_predator = predator[:3]  # mengambil dari awal sampai index 2
print(sliced_predator)
#Outputnya adalah: ['Lion', 'Tiger', 'Crocodile']

sliced_predator = predator[1:]  # mengambil dari index 1 sampai akhir
print(sliced_predator)
#Outputnya adalah: ['Tiger', 'Crocodile']

predator = ["Lion", "Tiger", "Crocodile"]
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

#TUPLE
colors = ("red", "green", "blue") 
print(colors[1])

#DICTIONARY
person = {"name": "sabian", "age": 30, "city": "New York"}
print(person) #output : {'name': 'sabian', 'age': 30, 'city': 'New York'}

person["age"] = 22 #add update
print(person) #output : {'name': 'sabian', 'age': 22, 'city': 'New York'}

person["job"] = "AI Engineer"  #nambah data
print(person) #output {'name': 'sabian', 'age': 22, 'city': 'New York', 'job': 'AI Engineer'}

del person["city"] #menghapus data
print(person) #output {'name': 'sabian', 'age': 22, 'job': 'AI Engineer'}

#iterasi dictionary
for key, value in person.items(): #yang bikin dia print ke bawah adalah .items()
  print(f"{key} : {value}") # key = name, age, job, value = sabian, 22, AI Engineer

#SETS (gabisa duplikat) (index disini tidak dipakai)
number = {1, 2, 3, 4}
number2 = {3, 4, 5, 6}

empty_set = set() #set kosong
print(number)
number.add(5)     #nambah data
print(number)     #output : {1, 2, 3, 4, 5}
number.add(4)     #gak nambah karena data nya ga bisa sama dengan data yang lainnya
print(number)     # output {1, 2, 3, 4, 5}
#number.remove(2) # untuk ngehapus
#print(number)    #output {1, 3, 4, 5}

number = {1, 2, 3, 4}
number2 = {3, 4, 5, 6}

print("union, gabungan dari 2 sets") #union (|) 
print(number | number2)   
print("intersection, data yang ada di 2 set ") #intersection (&) 
print(number & number2) 
print("difference, data yang ada di set 1 tapi ga ada di set 2")   #difference (-) 
print(number - number2)



#EXERCISE 