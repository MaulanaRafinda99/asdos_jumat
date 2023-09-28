# 1. Membuat dan mengisi nilai array 2 Dimensi.
# 2. Mengakses & Menampilkan isi nilai array 2 Dimensi.
# 3. Mengubah nilai dari array 2 dimensi.
# 4. Menghapus nilai dari array 2 dimensi.

arrayAngka = [[1,2,3],
              [4,5,6],
              [7,8,9]]

# 2. Mengakses & Menampilkan isi nilai array 2 Dimensi.
print(arrayAngka);

# 1 2 3
# 4 5 6 
# 7 8 9 

# Perulangan for : 
for baris in arrayAngka:
    for kolom in baris:
        print(kolom, end= " ");
    print();

# Menampilkan isi array sesuai keinginan :
print(arrayAngka[1]);
print(arrayAngka[2][2]);

# 3. Mengubah nilai dari array 2 dimensi.
arrayAngka[0] = [10,20,30];
print(arrayAngka);
arrayAngka[1][1] = 50;
print(arrayAngka);

# 4. Menghapus nilai dari array 2 dimensi.
print ("Hasil array ketika dilakukan proses del / hapus :")
del arrayAngka[2][1];
print(arrayAngka);



