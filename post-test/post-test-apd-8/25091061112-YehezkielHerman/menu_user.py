from clean import clear, tampilkan_tabel
from data import characterepep_bro

def menu_user(username):
    keluar_user = False
    while not keluar_user:
        clear()
        print(f"===== MENU USER <{username}> =====")
        print("1. Lihat Character")
        print("2. Logout")
        pilih_user = input("Pilih menu: ").strip()

        if pilih_user == "1":
            clear()
            if not characterepep_bro:
                print("Tidak ada character bro")
            else:
                print("\n===== DAFTAR CHARACTER EPEP =====")
                tampilkan_tabel()
            input("\nTekan Enter untuk kembali...")
        elif pilih_user == "2":
            keluar_user = True
        else:
            print("Pilihan tidak ada bro")
            input("\nTekan Enter untuk kembali...")
