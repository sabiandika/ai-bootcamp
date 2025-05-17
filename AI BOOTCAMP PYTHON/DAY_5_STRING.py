#concatenation
satu = "Hello"
dua = "World"
hasil = satu + " " + dua
print(hasil)

#SLICING
text = "Python Programming"
print(text[0:6]) # [0:6] akan print index 0 sampai 6 (Python)
print(text[-11:]) #[-11:] akan print sebelas index namun karena ada - jadi dimulai dari akhir (Programming)

#FORMATTING
# name = input("enter your name: ")
# age = input("Enter your age: ")
# job = input("Enter your job: ")
#print(f"Hello my name is {name} and i am {age} i work as {job}")

#SPLIT () 
kalimat = "Matematika ilmu yang mematikan"
kata = kalimat.split() #auto misahkan setiap kata dengan (,)
print(kata) #output ['Matematika', 'ilmu', 'yang', 'mematikan']

#JOIN()
kalimat1 = "|".join(kata)
print(kalimat1)