nama_benda = [];

for x in range(5):
    nama_benda.append(input("Input nama benda :"));

print("Hasil input nama benda : ");
print("");

for benda, nama_benda_input in enumerate(nama_benda,1):
    print("Benda :",benda, nama_benda_input);