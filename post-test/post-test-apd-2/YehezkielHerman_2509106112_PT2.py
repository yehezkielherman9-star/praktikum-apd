print("=" * 50)
print("TOKO BANGUNAN KIEL" .center(45))
print("=" * 50)

harga_batu_bata = 100
harga_semen = 100000

nama_pelanggan=(input("nama pelanggan : "))
print("=" * 50)

print("bahan  |  harga   |  jumlah    ")
print(f"batu   |Rp{harga_batu_bata}     |", end=" ")
jumlah_batu_bata=int(input(""))

print(f"batu   |Rp{harga_semen:,} |".replace(",", "."),  end=" ")
jumlah_karung_semen=int(input(""))
print("=" * 50)


total_harga=(jumlah_batu_bata*harga_batu_bata)+(jumlah_karung_semen*harga_semen)

if jumlah_batu_bata == 2000 and jumlah_karung_semen == 16:
    diskon  = 0.30
    jenis_paket = "SELAMATT ANDAA MENDAPATKANN DISKON ULTRAA MANTAPPP MANIAA"
elif jumlah_batu_bata == 500 and jumlah_karung_semen == 5:
    diskon = 0.15
    jenis_paket = "SELAMATT ANDA MENDAPATKANNN DISKONN HEMATT BANGETTT"
else:
    diskon= 0.0
    jenis_paket= "MAAF ANDA BELUM BERUNTUNG"

total_setelah_diskon = total_harga * (1 - diskon)

print("=" * 50)
print("ESTIMASI BIAYA BAHAN BANGUNAN" .center(45))
print("=" * 50)
print("=" * 50)

print(f"paket diskon                   : {jenis_paket}")  
print(f"total biaya awal               : Rp{total_harga:,}".replace(",", "."))
print(f"diskon                         : {int(diskon*100)}%")  
print("=" * 50)
print(f"total biaya akhir               : Rp{int(total_setelah_diskon):,}".replace(",", "."))
print("=" * 50)