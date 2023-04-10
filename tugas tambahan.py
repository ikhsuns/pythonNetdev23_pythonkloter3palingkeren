string = str(input("Masukkan string: "))

# Mengonversi string menjadi list karakter dan mengurutkannya
sorted_list = sorted(list(string))

# Menggabungkan kembali karakter dalam list menjadi sebuah string
sorted_string = "".join(sorted_list)

print("String yang diurutkan berdasarkan abjad: ", sorted_string)