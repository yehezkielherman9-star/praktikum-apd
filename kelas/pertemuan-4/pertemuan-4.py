ulangi = 10
for i in range (ulangi):
    print(f'Perulangan ke {i}')

simpan = [1, 'Dapupu', 4.00, True]
for i in simpan:
    print(i)

n = 10
for i in range (2,10):
    print(f"perulangan ke {i}")

for i in range(1, 4):# Mengontrol baris dalam tabel perkalian
    for j in range(1, 5):# Mengontrol kolom dalam tabel perkalian
        print(f'{i} x {j} = {i * j}')
    print('') #biar ada jarak tiap iterasi