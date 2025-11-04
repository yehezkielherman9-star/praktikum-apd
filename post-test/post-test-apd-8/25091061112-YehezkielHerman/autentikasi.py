from data import dataepep_bro
from clean import clear
from menu_admin import menu_admin
from menu_user import menu_user

def login():
    clear()
    print("=== LOGIN ===")
    username = input("Masukkan username: ").upper()
    password = input("Masukkan password: ")

    if username in dataepep_bro and dataepep_bro[username]["password"] == password:
        print(f"Selamat datang, {username}!")
        input("Tekan Enter untuk lanjut...")
        user = dataepep_bro[username]
        if user["role"] == "ADMIN":
            menu_admin()
        else:
            menu_user(username)
    else:
        print("Username atau password salah!")
        input("Tekan Enter untuk coba lagi...")

def register():
    clear()
    print("=== REGISTER ===")
    username = input("Masukkan username baru: ").upper()

    if username in dataepep_bro:
        print("Username sudah terdaftar!")
        input("Tekan Enter untuk kembali...")
        return

    password = input("Masukkan password baru: ")

    dataepep_bro[username] = {"password": password, "role": "USER"}
    print("Registrasi berhasil! Silakan login.")
    input("Tekan Enter untuk lanjut...")
