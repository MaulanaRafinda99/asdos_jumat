#buatlah array 2 dimensi dengan isi 5 baris& 5 kolom 
arrayAngka=[ [1 ,2 ,3, 4, 5],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25],
            [26,27,28,29,30]]

print (arrayAngka); # untuk memanggil/mencetak array angkanya
print ("======================") #untuk memperindah tampilan 

#ubah nilai index baris 3
print ("ubah nilai index baris ke 3")#untuk mencetak ubah nilainya 
arrayAngka [3] = [500,600,700,800,900]#untuk memanggil baris ke 3 dan angkanya telah dirobah 
print (arrayAngka);
print ("======================")

#hapus nilai baris pertama 
print ("hapus baris yang pertama")#perintah untuk memanggil hapus baris pertama 
del arrayAngka [0];#untuk menghapus angka nilai pada baris pertama 
print (arrayAngka);#untuk menampilkan angka 
print ("========================")

#tampilkan ke layar dengan menggunakan perulangan for:
for baris in arrayAngka:# untuk menampilkan bagian untuk baris dari kolom
    for kolom in baris: # untuk menampilkan bagian untuk kolon dari baris 
        print (kolom,end=" ");#perintah untuk menampilkan kolom 
    print (); #untuk ngeprint baris dan kolomnya