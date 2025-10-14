import os 

dataepep_bro = [
    ['ADMIN', 'minmin09' , 'ADMIN'],
    ['KIEL', 'kiel09', 'USER']
]

characterepep_bro = [
    ['Kelly','Deadly Velocity', 'Perempuan'],
    ['Alok', 'Drop The Beat', 'Pria'],
    ['Hayato', 'Bushido', 'Pria']]

def bersihin():
    os.system("cls" if os.name == "nt" else "bersihin")


def create_charepep():
    print("\n===== CREATE CHARACTER  =====")
    nama = input("Nama character : ").strip()
    skill = input("Skill character: ").strip()
    gender = input("Gender character: ").strip()
    
    if not nama or not skill or not gender:
        print("mana kok gak di isi")
        return
    
    characterepep_bro.append([nama, skill, gender])
    print(f"character {nama} berhasil di buat")

def listepep_bro():
        if not characterepep_bro:
            print("epep belum memiliki Character")
            
        else:
            print("\n=====  DAFTAR CHARACTER EPEP  =====")
            print(f"{'No':<4}| {'Nama':<20}| {'Skill':<25}| {'Gender':<10}|")
            print("-" * 65)

            for i, char in enumerate(characterepep_bro):
                print(f"{i+1:<4}| {char[0]:<20}| {char[1]:<25}| {char[2]:<10}|")
                print("-" * 65)


def updatechar_epep():
    listepep_bro()
    if not characterepep_bro:
        return
    nomorchar = input("\npilih nomor berapa character epep yang mau di update: ").strip()
    
    if not nomorchar.isdigit():
        print("pake angka bro")
        return
    nomorchar= int(nomorchar) - 1

    if nomorchar < 0 or nomorchar >= len(characterepep_bro):
        print("angka gak ada!!")
        return
    
    print("===== UPDATE CHARACTER =====")
    nama = input("Nama baru: ").strip()
    skill = input("skill baru: ").strip()
    gender = input("gender baru: ").strip()

    if not nama or not skill or not gender:
        print("mana kok gak di isi")
        return
    
    characterepep_bro[nomorchar] = ([nama, skill, gender])
    print("character sudah terbaharui")

def hapuschar_epepbro():
    listepep_bro()
    if not characterepep_bro:
        return
    
    print("===== HAPUS CHARACTER =====")
    nomorchar = input("\npilih nomor berapa character epep yang mau dihapus: ").strip()

    if not nomorchar.isdigit():
        print("pake angka bro")
        return
    nomorchar= int(nomorchar) - 1

    if nomorchar < 0 or nomorchar >= len(characterepep_bro):
        print("angka gak ada!!")
        return
    
    del characterepep_bro[nomorchar]
    print("character berhasil dihapus bro")

def regis():
    bersihin()
    print("===== REGISTER AKUN =====")
    username = input("Masukkan username baru anda: ").strip()
    pw = input("Masukkan password anda: ").strip()

    for userbaru in dataepep_bro:
        if userbaru[0] == username:
            print("username sudah ada")
            return
        
    dataepep_bro.append([username, pw, "USER"])
    print("""registrasi anda berhasil\nsilahkan login""")

def login():
    bersihin()
    print("===== LOGIN =====")
    username = input("Username: ").strip()
    pw = input("Password: ").strip()

    for user in dataepep_bro:
        if user[0] == username and user[1] == pw:
            print(f"Selamat datang, {username}!")
            return user
    print("Username atau password salah!")
    return None

def menu_sangadmin():
    while True:
        bersihin()
        print("===== MENU ADMIN =====")
        print("1. List Character")
        print("2. Create Character")
        print("3. Update Character")
        print("4. Hapus Character")
        print("5. Logout")
        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            bersihin()
            listepep_bro()
            input("\nTekan Enter untuk kembali...")
        elif pilih == "2":
            bersihin()
            create_charepep()
            input("\nTekan Enter untuk kembali...")
        elif pilih == "3":
            bersihin()
            updatechar_epep()
            input("\nTekan Enter untuk kembali...")
        elif pilih == "4":
            bersihin()
            hapuschar_epepbro()
            input("\nTekan Enter untuk kembali...")
        elif pilih == "5":
            print("anda berhasil logout")
            break
        else:
            print("Pilihan tidak ada bro!")

def menu_userbro(username):
    while True:
        bersihin()
        print(f"===== MENU USER <{username}> =====")
        print("1. List Karakter")
        print("2. Logout")
        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            bersihin()
            listepep_bro()
            input("\nTekan Enter untuk kembali...")
        elif pilih == "2":
            print("anda berhasil logout")
            break
        else:
            print("Pilihan tidak ada bro!")

while True:
    bersihin()
    print("===== SISTEM LIST CHARACTER GAME EPEP =====")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ").strip()

    if pilih == "1":
        user = login()
        if user:
            if user [2] == "ADMIN":
                menu_sangadmin()    
            else:
                menu_userbro(user[0])
    elif pilih == "2":
        regis()
        input("\nTekan Enter untuk kembali...")
    elif pilih == "3":
        bersihin()
        print("Terima kasih bro karena sudah menggunakan program ini")
        break
    else:
        print("Pilihan tidak ada bro!")
        input("\nTekan Enter untuk kembali...")
    
