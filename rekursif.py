# def function_biodata(nama, umur):
#     print(f"Halo nama saya adalah {nama}, dan saya berumur {umur} tahun.")

# function_biodata("Maulana Rafinda", 22);

# def rekursif():
#     print("Hello World...")
#     # Memanggil dirinya sendiri :
#     rekursif() # --> Rekusifitas

# # Memanggil function untuk pertama kali
# rekursif() 

def rekursif(batas, i = 1):
    print(f"Perulangan ke {i}")

    if (i < batas):
        rekursif(batas, i + 1)

rekursif(2)