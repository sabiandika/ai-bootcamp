#UNTK NGITUNG ADA BERAPA BARIS DAN BERAPA KATA
def count_words_and_lines(filename): #Mendefinisikan sebuah fungsi bernama count_words_and_lines dengan parameter filename, yaitu nama file yang ingin dibaca.

  try: #ntuk menangani error, khususnya jika file tidak ditemukan. Kalau ada error, program akan loncat ke bagian except.
    with open(filename, "r") as file:   #with agar file otomatis ditutup setelah digunakan ,file = nama variabel
      lines = file.readlines()   #menyimpan semua baris file ke dalam variable lines
      line_count = len(lines)    # Menghitung jumlah baris dengan menghitung panjang list lines (jumlah elemen di dalamnya).
      word_count = sum(len(line.split()) for line in lines) #line.split() akan memecah setiap baris menjadi list kata (dengan pemisah default: spasi).  
      #len(line.split()) menghitung jumlah kata dalam baris itu.
      #sum(...) for line in lines akan menjumlahkan total kata dari semua baris.
      print(f"Number of lines: {line_count}")
      print(f"Number of words: {word_count}")
  except FileNotFoundError:  # file yang error pada try akan terlempar ke except 
    print(f"File {filename} Not Found")

count_words_and_lines("random.txt") #memanggil fungsi count.. dan file random.txt untuk input. Dan fungsi akan coba membaca dan menghitung baris dan kata dari file tsb.



# Menulis dan membaca file
def write_item_to_file(filename, items): #Mendefinisikan sebuah fungsi bernama write_to _file dengan parameter filename dan items, yaitu nama file dan isi file yang ingin ditulis.
  with open(filename, "w") as file: #with agar file otomatis ditutup setelah digunakan. 
    for item in items: #mengulang setiap item di dalam list items.
      file.write (item + "\n") #menulis item ke dalam file, dengan pemisah baris baru ke bawah (\n) setiap item.

def read__item_to_file(filename):
  try: #ntuk menangani error, khususnya jika file tidak ditemukan. Kalau ada error, program akan loncat ke bagian except.
    with open(filename, "r") as file:   #with agar file otomatis ditutup setelah digunakan ,file = nama
      items = file.readlines()
      print("Items in the file:")
      for item in items:
        print(item.strip()) #strip() untuk menghilangkan spasi di awal dan akhir setiap item. 
  except FileNotFoundError:  # file yang error pada try akan terlempar ke except
    print(f"File {filename} Not Found") 

items = ["Apple", "Banana" "Cherry" "Date"]
Write_item_to_file ("fruits.txt",)
read_item_from_file ("fruits.txt")