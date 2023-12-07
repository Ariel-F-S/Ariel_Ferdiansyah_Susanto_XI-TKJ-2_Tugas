# Nama      : Ariel Ferdiansyah Susanto
# Kelas     : XI-TKJ 2
# No. Absen : 04

# SOAL : Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan dengan eksponen tertentu.

def eksponen(angka , pangkat):
    hasil = 1
    for _ in range(pangkat):
        hasil *= angka
    return hasil

angka = float(input("Masukkan angka: "))
pangkat = int(input("Masukkan bilangan pangkat eksponen: "))

print(f"Hasil dari perkalian {angka}^{pangkat} adalah {eksponen(angka, pangkat)}")