# Inisialisasi variabel array kosong :
merek_HP = [];

# Membuat perulangan untuk input :
for x in range(5):
    merek_HP.append(input("Masukan merek HP :" ));

print("==========================================");

# Membuat perulangan untuk menampilkan data :
for merek, hasil_input_merek in enumerate(merek_HP,1):
    print("Merek :",merek,hasil_input_merek);

# Buat variabel kosong untuk menginput 5 nama_warna :
