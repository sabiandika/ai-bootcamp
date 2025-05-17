#REGULAR EXPRESSION (REGEX)
import re

# r"\d" adalah regex:
# \d berarti 1 digit angka (0 sampai 9)
# r"" adalah raw string agar Python tidak memproses backslash (\) sebagai escape character.
# \D adalah kebalikan dari \d, yaitu karakter

text = "Contact me at 0812-1231-9099"
digit = re.findall(r"\d+", text) #mencari semua urutan digit angka (yaitu satu atau lebih digit, karena +).
print(digit ) #output ['0812', '1231', '9099']

update_text = re.sub(r"\d", "X", text) #mengubah bilangan angka/integer menjadi X
print(update_text) #output Contact me at XXXX-XXXX-XXXX

#EXERCISE 
#import re

def clean_text(text):
  text = re.sub(r"[^\w\s]", "", text) 
  text = " ".join(text.split()) #.split untuk
  return text.lower()

input_text = "    Hello, world!!? Welcome to Python, programming..."
cleaned_text = clean_text(input_text)
print("Cleaned Text: ",cleaned_text)


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
kalimat1 = "|".join(kata) #berfungsi untuk menambahkan apa yang ingin ditambahakan
print(kalimat1)

#REPLACE
text = "i love java"
update_text = text.replace("love", "python") #untuk mengganti string contoh love diganti java
print(update_text) # output i python java

#MERAPIHKAN TEXT
messy = "       I Love python          "
print(messy) #sebelum dirapihkan output=        I Love python
cleaned_text = messy.strip()
print(cleaned_text) #sesudah sirapihkan output=I Love python

