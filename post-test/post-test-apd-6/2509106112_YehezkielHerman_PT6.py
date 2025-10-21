import os

dataepep_bro = {
    "ADMIN": {"password": "minmin09", "role": "ADMIN"},
    "KIEL": {"password": "kiel09", "role": "USER"}
}

characterepep_bro = {
    1: {"nama": "Kelly", "skill": "Deadly Velocity", "gender": "Perempuan"},
    2: {"nama": "Alok", "skill": "Drop The Beat", "gender": "Pria"},
    3: {"nama": "Hayato", "skill": "Bushido", "gender": "Pria"}
}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("===== SISTEM LIST CHARACTER GAME EPEP =====")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ").strip()

    if pilih == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("===== REGISTER AKUN =====")
        username = input("Masukkan username baru anda: ").strip()
        pw = input("Masukkan password anda: ").strip()

        if username in dataepep_bro:
            print("Usernamenya sudah ada")
        else:
            dataepep_bro[username] = {"password": pw, "role": "USER"}
            print("Registrasi berhasil, silakan login")

        input("\nTekan Enter untuk kembali...")

    elif pilih == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("===== LOGIN =====")
        username = input("Username: ").strip()
        pw = input("Password: ").strip()

        user_login = None
        if username in dataepep_bro and dataepep_bro[username]["password"] == pw:
            user_login = {"username": username}
            user_login.update(dataepep_bro[username])

        if user_login == None:
            print("Username atau password nya salah")
            input("\nTekan Enter untuk kembali...")
        else:
            print(f"Selamat datang, {username}!")
            input("\nTekan Enter untuk lanjut...")

            if user_login["role"] == "ADMIN":
                keluar_admin = False
                while not keluar_admin:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("===== MENU ADMIN =====")
                    print("1. List Character")
                    print("2. Create Character")
                    print("3. Update Character")
                    print("4. Hapus Character")
                    print("5. Logout")
                    pilih_admin = input("Pilih menu: ").strip()

                    if pilih_admin == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        if not characterepep_bro:
                            print("engga ada character nya bro")
                        else:
                            print("\n===== DAFTAR CHARACTER EPEP =====")
                            print(f"{'No':<4}| {'Nama':<20}| {'Skill':<25}| {'Gender':<10}|")
                            print("-" * 65)
                            for nomor, char in characterepep_bro.items():
                                print(f"{nomor:<4}| {char['nama']:<20}| {char['skill']:<25}| {char['gender']:<10}|")
                                print("-" * 65)
                        input("\nTekan Enter untuk kembali...")

                    elif pilih_admin == "2":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\n===== CREATE CHARACTER =====")
                        nama = input("Nama character: ").strip()
                        skill = input("Skill character: ").strip()
                        gender = input("Gender character: ").strip()

                        if not nama or not skill or not gender:
                            print("Semua data nya harus diisi kocak")
                        else:
                            if characterepep_bro:
                                nomor_baru = max(characterepep_bro.keys()) + 1
                            else:
                                nomor_baru = 1
                            characterepep_bro[nomor_baru] = {"nama": nama, "skill": skill, "gender": gender}
                            print(f"Character {nama} berhasil dibuat")
                        input("\nTekan Enter untuk kembali...")

                    elif pilih_admin == "3":
                        os.system("cls" if os.name == "nt" else "clear")
                        if not characterepep_bro:
                            print("Belum ada character nya untuk diubah bro!")
                            input("\nTekan Enter untuk kembali...")
                        else:
                            print("===== UPDATE CHARACTER =====")
                            for nomor, char in characterepep_bro.items():
                                print(f"{nomor:<4}| {char['nama']:<20}| {char['skill']:<25}| {char['gender']:<10}|")
                                print("-" * 65)

                            nomorchar = input("\nPilih nomor character nya yang mau diupdate: ").strip()
                            if not nomorchar.isdigit():
                                print("pake angka bro")
                            else:
                                nomor = int(nomorchar)
                                if nomor not in characterepep_bro:
                                    print("character nya tidak ada")
                                else:
                                    nama = input("Nama baru: ").strip()
                                    skill = input("Skill baru: ").strip()
                                    gender = input("Gender baru: ").strip()
                                    if not nama or not skill or not gender:
                                        print("Semua data nya harus diisi dong")
                                    else:
                                        characterepep_bro[nomor] = {"nama": nama, "skill": skill, "gender": gender}
                                        print("Character epep mu sudah berhasil diupdate")
                            input("\nTekan Enter untuk kembali...")

                    elif pilih_admin == "4":
                        os.system("cls" if os.name == "nt" else "clear")
                        if not characterepep_bro:
                            print("engga ada character nya untuk dihapus")
                        else:
                            print("===== HAPUS CHARACTER =====")
                            for nomor, char in characterepep_bro.items():
                                print(f"{nomor:<4}| {char['nama']:<20}| {char['skill']:<25}| {char['gender']:<10}|")
                                print("-" * 65)
                            nomorchar = input("\nPilih nomor character nya yang mau dihapus: ").strip()
                            if not nomorchar.isdigit():
                                print("pake angka dong")
                            else:
                                nomor = int(nomorchar)
                                if nomor not in characterepep_bro:
                                    print("character nya enggak ada")
                                else:
                                    del characterepep_bro[nomor]
                                    print("Character epep mu berhasil dihapus")
                        input("\nTekan Enter untuk kembali...")

                    elif pilih_admin == "5":
                        print("kamu berhasil logout")
                        keluar_admin = True
                    else:
                        print("Pilihan mu tidak ada kocak!")
                        input("\nTekan Enter untuk kembali...")

            else:
                keluar_user = False
                while not keluar_user:
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"===== MENU USER <{username}> =====")
                    print("1. List character nya")
                    print("2. Logout")
                    pilih_user = input("Pilih menu: ").strip()

                    if pilih_user == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        if not characterepep_bro:
                            print("enggak ada character nya nya loh")
                        else:
                            print("\n===== DAFTAR CHARACTER EPEP =====")
                            print(f"{'No':<4}| {'Nama':<20}| {'Skill':<25}| {'Gender':<10}|")
                            print("-" * 65)
                            for nomor, char in characterepep_bro.items():
                                print(f"{nomor:<4}| {char['nama']:<20}| {char['skill']:<25}| {char['gender']:<10}|")
                                print("-" * 65)
                        input("\nTekan Enter untuk kembali...")

                    elif pilih_user == "2":
                        print("kamu berhasil logout loh")
                        keluar_user = True
                    else:
                        print("Pilihan gak ada bro")
                        input("\nTekan Enter untuk kembali...")

    elif pilih == "3":
        os.system("cls" if os.name == "nt" else "clear")
        print("Terima kasih karena sudah menggunakan program ini bro")
        break

    else:
        print("Pilihan tidak ada kocakk")
        input("\nTekan Enter untuk kembali...")
