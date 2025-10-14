kelas = ['rido', 20, True, 45.50, ['apd', 25]]

print(kelas [4])

studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# Tambahkan Web
studyclub.append("Web")
print(studyclub)

studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# Tambahkan Web
studyclub.insert(1,"Web")
print(studyclub)

# list awal
studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
print(studyclub)
# Kita akan mengganti elemen di indeks ke-2, yakni "Multimedia"
studyclub[2] = "AI"
print(studyclub)

matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
print(matakuliah)
# menghapus elemen pada indeks ke-2, yakni "Kalkulus"
del matakuliah[2]
print(matakuliah)

# list awal
matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
print(matakuliah)
# menghapus elemen dengan nilai "Kalkulus"
matakuliah.remove('Kalkulus')
print(matakuliah)

# list awal
matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
print(matakuliah)
# Menghapus & mengambil elemen 'Kalkulus' pada indeks ke-2
ambil_matkul = matakuliah.pop(2)
print(matakuliah)
print(ambil_matkul)

# list
matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
'Orsikom','Basis Data']
# Menampilkan list mulai dari indeks 1 hingga 5 dengan loncatan 2
print(matakuliah[0:6:3])

# List
a = [1, 2, 3]
b = [4, 5, 6]
# menggabungkan kedua list dengan operator (+)
c = a + b
print(c)

a = ["teknik", "informatika"]
# mengulang isi list dengan operator (*) sebanyak 3 kali
c = a*3
print(c)

kelas = [
["Ridho", "Lian", "Nabil"],
["Daffa", "Dante", "Santoso"],
["Pernanda", "Riyadi", "Ahnaf"],
]
print(kelas[1])

# list mahasiswa
mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]
# perulangan for untuk mendapatkan semua elemen
for i in mahasiswa:
    for j in i :
        print (j)
# /i dan j merupakan variabel sementara / temporary, kita dapat menggantinya
# dengan apa saja asal sesuai dengan syarat nama variabel

#mendefinisikan tuple
anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
print(anggota)

# menampilkan tuple
anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
# memanggil satu elemen
print(anggota[1])
print(anggota[-1])
# memanggil elemen di dalam nested tuple
print(anggota[5][0])

# list awal
studyclub = ("Data Science", "Robotics", "Multimedia", "Network")
liststudy=list(studyclub)
# Tambahkan Web
liststudy.append("Web")
studyclub=tuple(liststudy)
print(studyclub)

# tuple awal
studyclub = ("Data Science", "Robotics", "Multimedia", "Network")
# Ubah tuple menjadi list
liststudy=list(studyclub)
# Tambahkan Web
liststudy.insert(2,"Web")
# ubah kembali list menjadi tuple
studyclub=tuple(liststudy)
print(studyclub)

# tuple awal
studyclub = ("Data Science", "Robotics", "Multimedia", "Network")
print(studyclub)
# Ubah tuple menjadi list
liststudy=list(studyclub)
# Kita akan mengganti elemen di indeks ke-2, yakni "Multimedia"
liststudy[2] = "AI"
# ubah kembali list menjadi tuple
studyclub=tuple(liststudy)
print(studyclub)

# tuple awal
hobi=("Futsal","Catur","Renang")
print(hobi)
# ubah tuple menjadi list
gemar=list(hobi)
# menghapus elemen pada indeks ke-2, yakni "Renang"
del gemar[2]
# Ubah list kembali menjadi tuple
hobi=tuple(gemar)
print(hobi)

# tuple awal
hobi=("Futsal","Catur","Renang")
print(hobi)
# ubah tuple menjadi list
gemar=list(hobi)
# menghapus elemen dengan nilai "catur"
gemar.remove("Catur")
# ubah list kembali menjadi tuple
hobi=tuple(gemar) 
print(hobi)  

tugas = ('rangkuman', 'arduino','scrapping')
# beri variabel setiap values
(PTI, orsikom, basisdata) = tugas
print(PTI)
print(orsikom)

barang = ('triangle','bola', 'meja', 'handphone', 'televisi')
# beri variabel setiap values
(segitiga, bulat, *kotak) = barang
print(segitiga)
print(bulat)
print(kotak[0])

# tuple
barang = ('triangle','bola', 'meja', 'handphone', 'televisi')
angka=(1,2,3)
# simpan di dalam variabel baru
gabung=barang+angka
print(gabung)

barang = [['triangle','bola'], ['meja', 'handphone'], ['televisi','laptop']]
for i in barang:
    print(i)
    (barang1, barang2) = i
    print(barang1)
    print(barang2)

# mahasiswa = [["jawa","batak"],[1],("toraja")]
# for i, maha in enumerate in mahasiswa:
#     if i == 2:
#     (maha1,maha2) = i
#     print(maha1)
#     print(maha2)
#     print("ini tupple")
#     else: