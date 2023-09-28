# Kita membuat sebuah program untuk menampilkan deret angka Fibonacci :
# Deret Fibonacci : 0 1 1 2 3 5 8 13 ...
# Deret Fibonacci berasal dari hasil penambahan suku n-1 dengan suku n-2.

def rekursif_fibonacci(n):
    if n <= 1:
        return n
    else: 
        return (rekursif_fibonacci(n-1) + rekursif_fibonacci(n-2));

n_kondisi = int(input("Masukan jumlah deret angka Fibonacci yang ingin ditampilkan :"))

# Cek kondisi untuk n_kondisi :
if n_kondisi < 0:
    # Nilai 20 Point : Danan
    print("Mohon masukan nilai bulat bilangan positif")
else:
    # Menampilkan deret angka dengan menggunakan perulangan for.
    for i in range(n_kondisi):
        print(rekursif_fibonacci(i))