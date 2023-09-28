# Menginput isi array dari terminal / menerima input dari user : 

# 1. Inisialisasi variabel array kosong;
nama_buah = [];

# 2. Membuah perulangan input sesuai dengan jumlah data yang akan diinput dengan perulangan for :
for i in range(5):
    nama_buah.append(input("Masukan nama buah :"));

print("============================================");
print(" ");

for buah, nama_buah_input in enumerate(nama_buah,1):
    print("Buah",buah, nama_buah_input);