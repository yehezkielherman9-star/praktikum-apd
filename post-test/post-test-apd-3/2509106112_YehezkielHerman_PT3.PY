print("="*60)
print("Penghitung Gaji Karyawan PT. BOM".center(60))
print("="*60)
nama_karyawan = str(input("nama karyawan = "))
jabatan_karyawan = str (input("""jabatan karyawan: 
(peracik petasan/pengantar petasan) = """))
hari_kerja = int(input("hari kerja = "))
jam_kerja = int(input("jam kerja = "))
jumlah_perlembur = int(input("jumlah perlembur = "))
print("-"*60)

if jabatan_karyawan == "peracik petasan":
    if hari_kerja >= 18 and jam_kerja >= 6 and jumlah_perlembur >= 2: 
        bayaran_perjam = 20000
        bayaran_perlembur = 10000
    elif hari_kerja >= 24 and jam_kerja >= 8 and jumlah_perlembur >= 2: 
        bayaran_perjam = 25000
        bayaran_perlembur = 15000
    else:
        bayaran_perjam = 15000
        bayaran_perlembur = 10000

elif jabatan_karyawan == "pengantar petasan":
    if hari_kerja >= 16 and jam_kerja >= 5 and jumlah_perlembur >= 4: 
        bayaran_perjam = 20000
        bayaran_perlembur = 15000
    elif hari_kerja >= 20 and jam_kerja >= 7 and jumlah_perlembur >= 7:
        bayaran_perjam = 25000
        bayaran_perlembur = 20000
    else:
        bayaran_perjam = 15000
        bayaran_perlembur = 12000

total_gaji = ((bayaran_perjam*jam_kerja)*hari_kerja)+(jumlah_perlembur*bayaran_perlembur)

print("="*60)
print("Penghitung Gaji Karyawan PT. BOM".center(60))
print("="*60)
print(f"Nama karyawan           :{nama_karyawan}")
print(f"Hari kerja              :{hari_kerja}")
print(f"Jam kerja               :{jam_kerja}")
print(f"Jumlah perlembur        :{jumlah_perlembur}")
print(f"Bayaran perjam          :Rp{bayaran_perjam:,}".replace(",","."))
print(f"Bayaran perlembur       :Rp{bayaran_perlembur:,}".replace(",","."))
print(f"Total gaji              :Rp{total_gaji:,}".replace(",","."))
print("-"*60)

