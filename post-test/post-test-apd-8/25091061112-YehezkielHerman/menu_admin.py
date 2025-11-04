from data import characterepep_bro
from clean import clear, tampilkan_tabel

def menu_admin():
    keluar_admin = False
    while not keluar_admin:
        clear()
        print("===== MENU ADMIN =====")
        print("1. List Character")
        print("2. Create Character")
        print("3. Update Character")
        print("4. Hapus Character")
        print("5. Logout")
        pilih_admin = input("Pilih menu: ").strip()

        if pilih_admin == "1":
            clear()
            if not characterepep_bro:
                print("Tidak ada character bro")
            else:
                print("\n===== DAFTAR CHARACTER EPEP =====")
                tampilkan_tabel()
            input("\nTekan Enter untuk kembali...")

        elif pilih_admin == "2":
            clear()
            print("\n===== CREATE CHARACTER =====")
            nama = input("Nama character: ").strip()
            skill = input("Skill character: ").strip()
            gender = input("Gender character: ").strip()

            if not nama or not skill or not gender:
                print("Semua data harus diisi bro!")
            else:
                nomor_baru = max(characterepep_bro.keys()) + 1 if characterepep_bro else 1
                characterepep_bro[nomor_baru] = {"nama": nama, "skill": skill, "gender": gender}
                print(f"Character {nama} berhasil dibuat")
            input("\nTekan Enter untuk kembali...")

        elif pilih_admin == "3":
            clear()
            if not characterepep_bro:
                print("Belum ada character untuk diubah")
                input("\nTekan Enter untuk kembali...")
            else:
                print("===== UPDATE CHARACTER =====")
                tampilkan_tabel()

                nomorchar = input("\nPilih nomor character yang mau diupdate: ").strip()
                if not nomorchar.isdigit():
                    print("Harus angka bro!")
                else:
                    nomor = int(nomorchar)
                    if nomor not in characterepep_bro:
                        print("Character tidak ditemukan")
                    else:
                        nama = input("Nama baru: ").strip()
                        skill = input("Skill baru: ").strip()
                        gender = input("Gender baru: ").strip()
                        if not nama or not skill or not gender:
                            print("Semua data wajib diisi bro!")
                        else:
                            characterepep_bro[nomor] = {"nama": nama, "skill": skill, "gender": gender}
                            print("Character berhasil diupdate")
                input("\nTekan Enter untuk kembali...")

        elif pilih_admin == "4":
            clear()
            if not characterepep_bro:
                print("Tidak ada character untuk dihapus")
            else:
                print("===== HAPUS CHARACTER =====")
                tampilkan_tabel()
                nomorchar = input("\nPilih nomor character yang mau dihapus: ").strip()
                if not nomorchar.isdigit():
                    print("Harus angka bro!")
                else:
                    nomor = int(nomorchar)
                    if nomor not in characterepep_bro:
                        print("Character tidak ditemukan")
                    else:
                        del characterepep_bro[nomor]
                        print("Character berhasil dihapus")
            input("\nTekan Enter untuk kembali...")

        elif pilih_admin == "5":
            keluar_admin = True
        else:
            print("Pilihan tidak ada bro!")
            input("\nTekan Enter untuk kembali...")
