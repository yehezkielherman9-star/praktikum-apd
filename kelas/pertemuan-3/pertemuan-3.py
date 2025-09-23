print("Hello World")
nilai = 75
if nilai == 75:
    print("Anda Lulus!") # Blok if dijalankan karena kondisi True
else:
    print("Anda Belum Lulus.") # Blok else tidak dijalankan

umur = int(input("Masukkan umur Anda: "))
# misalnya, umur = 16
# Percabangan
if umur < 13:
    kategori = "Anak-anak"
elif umur < 18:
    kategori = "Remaja"
elif umur < 60:
    kategori = "Dewasa"
else:
    kategori = "Lansia"
# Menampilkan umur dan kategori
print("Umur:", umur, "Kategori:", kategori)

nilai = 70
if nilai == 60:
    status = "Lulus"

else:
    status = "Tidak Lulus"
print(status)

# Menggunakan Ternary Operator
nilai = 70
status = "Lulus" if nilai == 60 else "Tidak Lulus"
print(status)