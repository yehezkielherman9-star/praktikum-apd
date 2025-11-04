from utils import clear, tampilkan_tabel
from data import characterepep_bro

def menu_user(username):
    try:
        keluar_user = False
        while not keluar_user:
            clear()
            print(f"===== MENU USER <{username}> =====")
            print("1. List character nya")
            print("2. Logout")
            pilih_user = input("Pilih menu: ").strip()

            if pilih_user == "1":
                clear()
                if not characterepep_bro:
                    print("enggak ada character nya nya loh")
                else:
                    print("\n===== DAFTAR CHARACTER EPEP =====")
                    tampilkan_tabel()
                input("\nTekan Enter untuk kembali...")

            elif pilih_user == "2":
                print("kamu berhasil logout loh")
                keluar_user = True
            else:
                print("Pilihan gak ada bro")
                input("\nTekan Enter untuk kembali...")

    except ValueError:
        print("Terjadi kesalahan di menu user: input harus berupa angka dong bro")
        input("\nTekan Enter untuk kembali...")
