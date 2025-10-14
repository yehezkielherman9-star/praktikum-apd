print ("1. misi pertama yaitu tes konsentrasi")

stamina = int(input("masukin stamina kalian berdasarkan dengan digit terakhir nim = "))

chakra =0

while chakra < 200 and stamina > 0:
        chakra += 5
        stamina -= 3
        if stamina < 0:
            stamina = 0

print(f"total chakra yang sudah terkumpul = {chakra}")
print(f"stamina yang tersisa = {stamina}")

if chakra == 200:
    print("anda berhasil menyempurnakan rasengan")
else:
    print("stamina anda telah habis!!")

print("2. misi kedua yaitu infiltrasi")

tinggi = int(input("masukkan tinggi menara dengan 2 digit nim terakhir = "))

jumlah_gulungan=0
for i in range(1, tinggi + 1, 3):
     jumlah_gulungan += 1
print(f"jumlah gulungan yang anda dapat = {jumlah_gulungan}")

print("3. Misi ketiga yaitu penyelidikan")

jumlah_koridor = int(input("masukkan jumlah koridor berdasarkan digit nim terakhir kedua = "))
 
data_intel = 0
perangkap = 0

for k in range (1, jumlah_koridor + 1):
    print(f"anda memasuki koridor = {k}")

    for r in range (1, 4):
        print (f"anda memasuki ruangan {r}")

        if r % 2 == 1:
            print("didalamnya ada data intelejen")
            data_intel += 1
        else:
            print("didalam nya berisi perangkap peledak")
            perangkap += 1

print("<<<<<MISI SELESAI>>>>>")
print(f"jumlah data intelejen yang telah di dapatkan {data_intel}")
print(f"jumlah perangkap peledak yang sudah dijinakkan {perangkap}")