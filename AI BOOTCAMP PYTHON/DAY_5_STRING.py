#REGULAR EXPRESSION (REGEX)
import re

# r"\d" adalah regex:
# \d berarti 1 digit angka (0 sampai 9)
# r"" adalah raw string agar Python tidak memproses backslash (\) sebagai escape character.
# \D adalah kebalikan dari \d, yaitu karakter
# \w = semua huruf (a-z, A-Z) dan angka (0-9) serta underscore (_)
# \s = spasi (whitespace)
# ^ = "kecuali"

text = "Contact me at 0812-1231-9099"
digit = re.findall(r"\d+", text) #mencari semua urutan digit angka (fungsi + untuk mengelompokkan angka),jika tidak ada + angka akan terpisah sendiri sendiri.
print(digit ) #output ['0812', '1231', '9099']

update_text = re.sub(r"\d", "X", text) #mengubah bilangan angka/integer menjadi X
print(update_text) #output Contact me at XXXX-XXXX-XXXX

#EXERCISE 1 MERAPIHKAN TEXT
#import re

def clean_text(text):
  text = re.sub(r"[^\w\s]", " ", text) # re.sub untuk menghapus dan mengecualikan(^) penghapusan karakater kecuali huruf,angka,_(\w),spasi(\s)
  text = " ".join(text.split()) #" " untuk menambahkan spasi setiap kata, .split() memecah teks menjadi daftar kata berdasarkan spasi (otomatis menghilangkan spasi berlebih).
  return text.lower() #untuk mengubah ke huruf kecil semua

input_text = "    Hello, world!!? Welcome to Python, programming..."
cleaned_text = clean_text(input_text)
print("Cleaned Text: ",cleaned_text)

#EXERCISE 2 APAKAH KATA ITU PALINDROM ATAU TIDAK, PALINDROM = KATA YANG TERBACA SAAT DIBALIK (RADAR)
def is_palindrome(kata):
  text = "".join(char.lower() for char in kata if char.isalnum())
  #char.lower() → mengubah ke huruf kecil, char.isalnum() → hanya ambil huruf dan angka, abaikan spasi/tanda baca.
  return text == text[::-1]  # → membalik teks untuk dicek apakah sama dengan aslinya.

input_text = input("Enter yout Palindrome: ")
if is_palindrome(input_text):
  print(f'"{input_text}" is a palindrome')
else:
  print(f'"{input_text}"is not palindrome')



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
name = input("enter your name: ")
age = input("Enter your age: ")
job = input("Enter your job: ")
print(f"Hello my name is {name} and i am {age} i work as {job}")

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

