buah = {"apel", "jeruk", "mangga", "apel"}
# buah = ([“apel”, “jeruk”, “mangga”, “apel”])   
print(buah)

angka_ganjil = {1, 3, 5, 7, 9}
for angka in angka_ganjil:
    print (angka)

inputTambah = int(input("tambah angka: "))
angka_ganjil.add(inputTambah)
print(angka_ganjil)

print(angka_ganjil)
inputTambah=int(input("tambah angka: "))
angka_ganjil.remove(inputTambah)
angka_ganjil.discard(inputTambah)
print(angka_ganjil)

Daftar_buku = {
"Buku1" : "Bumi Manusia",
"Buku2" : "Laut Bercerita"
}
print(Daftar_buku["Buku1"])
print(Daftar_buku)

# Contoh
Biodata = {
"Nama" : "Ananda Daffa Harahap",
"NIM" : 2409106050,
"KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
"Mahasiswa_Aktif" : True,
"Social Media" : {"Instagram" : "daffahrhap"}
}   

print(f"nama saya adalah {Biodata["Nama"]}")
print(f"Instagram : {Biodata['Social Media']['Instagram']}")

print(f"nama saya adalah {Biodata.get("Nama")}")
print(Biodata.get("Nama"))

print(Biodata.get("Alamat"))
print(Biodata.get("Alamat", "key ini tidak ada"))

Nilai = {
"Matematika": 80,
"B. Indonesia": 90,
"B. Inggris": 81,
"Kimia": 78,
"Fisika": 80,
}
# Tanpa menggunakan items()
for i in Nilai:
    print(i)
print("") # pemisah
# Menggunakan items()
for key, value in Nilai.items():
    print(f"Nilai {key} anda adalah {value}")

Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}
print(Film)
Film["Zombieland"] = "Comedy"
Film.update({"Hours" : "Thriller"})
#Setelah Ditambah
print(Film)

Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}
#Sebelum Diubah
print(Film)
Film["Sherlock Holmes"] = "Action"
Film.update({"The Conjuring" : "Tragedy"})
print(Film)

data = {
"Nama" : "Daffa",
"Umur" : 19,
"Jurusan" : "Informatika"
}
#Sebelum Dihapus
print(data)
del data["Nama"]

print(data)

print(data.get("Nama"))
{'Nama': 'Daffa', 'Umur': 19, 'Jurusan': 'Informatika'}
{'Umur': 19, 'Jurusan': 'Informatika'}

print(data)

data = {
"Nama" : "Daffa",
"Umur" : 19,
"Jurusan" : "Informatika"
}
#Sebelum Dihapus
print(data)
cache = data.pop("Nama")
#Setelah dihapus
print(data)
#memanggil data yang telah dihapus pada dictionary
print(data.get("Nama"))
#memanggil data yang telah dihapus pada variabel cache
print(cache)

data = {
"Nama" : "Daffa",
"Umur" : 19,
"Jurusan" : "Informatika"
}
#Sebelum Dihapus
print(data)
data.clear()
#Setelah dihapus
print(data)

data = {
"Nama" : "Daffa",
"Umur" : 19,
"Jurusan" : "Informatika"
}
print("Jumlah Data = ", len(data))

buku = {
"Buku1" : "Bumi Manusia",
"Buku2" : "Laut Bercerita"
}
pinjam = buku.copy()
print("Dictionary yang telah disalin : ", pinjam)

key = "apel", "jeruk", "mangga"
value = 1
buah = dict.fromkeys(key, value)
print(buah)

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81,
"Kimia" : 78,
"Fisika" : 80
}
#menggunakan keys
for i in Nilai.keys():
    print(i)
print("")
#menggunakan value
for i in Nilai.values():
    print(i)

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}
#sebelum Setdefault
print(Nilai)
print (len(Nilai))
print("")
#menggunakan setdefault
print("Nilai : ", Nilai.setdefault("Kimia", 70))
print("Nilai : ", Nilai.setdefault("Matematika", 90))

print("")
#setelah menggunakan setdefault
print(Nilai)
print (len(Nilai))

Musik = {
"The Chainsmoker" : ["All we Know", "The Paris"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}
for i, j in Musik.items():
    print(f"Musik milik {i} adalah : ")
    for song in j:
        print(song)
print("")