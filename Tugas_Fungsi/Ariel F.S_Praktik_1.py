# Nama      : Ariel Ferdiansyah Susanto
# Kelas     : XI-TKJ 2
# No. Absen : 04

# SOAL : Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga batas tertentu yang ditentukan pengguna.


akhir =  int(input("Mausukkan angka ganjil: "))

def deret_ganjil(akhir):
    total = 0
    for i in range (1, akhir +1, 2):
        total += 1
    return total

print(f"Total bilangan ganjil pada deret tersebut ", akhir, "adalah", deret_ganjil(akhir))