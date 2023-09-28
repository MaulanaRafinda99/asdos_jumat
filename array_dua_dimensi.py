# Topik Belajar Kita hari ini :
# 1. Membuat & mengisi Array dua dimensi :
# 2. Mengakses & mencetak Array dua Dimensi :
# 3. Mengubah nilai Array dua Dimensi :
# 4. Menghapus nilai Array dua Dimensi : 


# 1. Membuat & mengisi Array dua dimensi :
arrayAngka = [[1,2,3],
              [4,5,6],
              [7,8,9]]

# 2. Mengakses & mencetak Array dua Dimensi :
print(arrayAngka);

print("Mencetak array : ");
for baris in arrayAngka:
    for kolom in baris:
        print(kolom, end= " ");
    print();

print(arrayAngka[1][1]);

# 3. Mengubah nilai Array dua Dimensi :
arrayAngka[0] = [3,2,1];
for baris in arrayAngka:
    for kolom in baris:
        print(kolom, end =" ");
    print();

# 4. Menghapus nilai Array dua Dimensi : 
print("Hasil setelah array sudah dihapus :");
del arrayAngka[1];

for baris in arrayAngka:
    for kolom in baris:
        print(kolom, end= " ");
    print();

