from utils import clear
from autentikasi import login, register
from menu_admin import menu_admin
from menu_user import menu_user

def main():
    while True:
        clear()
        print("=== Selamat Datang di Sistem Free Fire Epep ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            user = login()
            if user:
                if user["role"] == "ADMIN":
                    menu_admin()
                else:
                    menu_user()
        elif pilihan == "2":
            register()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk lanjut...")

main()
