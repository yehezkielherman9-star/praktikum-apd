from clean import clear
from autentikasi import login, register

def main():
    while True:
        clear()
        print("===== SISTEM LIST CHARACTER GAME EPEP =====")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            login()
        elif pilih == "2":
            register()
        elif pilih == "3":
            clear()
            print("Terima kasih sudah menggunakan program ini bro!")
            break
        else:
            print("Pilihan tidak ada bro!")
            input("\nTekan Enter untuk kembali...")

main()
