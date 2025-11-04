import os
from prettytable import PrettyTable
from data import characterepep_bro

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_tabel():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Skill", "Gender"]
    for nomor, char in characterepep_bro.items():
        tabel.add_row([nomor, char["nama"], char["skill"], char["gender"]])
    print(tabel)
