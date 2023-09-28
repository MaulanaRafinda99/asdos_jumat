# def my_function():
#     print("Hello python...")
#     # Memanggil dirinya sendiri :
#     my_function() # --> Rekursifitas.

# # Memanggil function untuk pertama kali.
# my_function();

def my_function(batas, i = 1):
    # Desy Gusnita Sari : 20 Point tugas.
    print(f"Perulangan ke {i}");

    if(i < batas):
        my_function(batas, i + 1);

my_function(5);