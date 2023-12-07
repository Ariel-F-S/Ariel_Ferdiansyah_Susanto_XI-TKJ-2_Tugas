<<<<<<< HEAD
# Nama      : Ariel Ferdiansyah Susanto
# Kelas     : XI-TKJ 2
# No. Absen : 04

# SOAL : Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)
    
angka = int(input("masukkan angka: "))
hasil_faktorial = faktorial(angka)

=======
# Nama      : Ariel Ferdiansyah Susanto
# Kelas     : XI-TKJ 2
# No. Absen : 04

# SOAL : Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)
    
angka = int(input("masukkan angka: "))
hasil_faktorial = faktorial(angka)

>>>>>>> c326b4335814a81d3d652480bc133b6024bcdd27
print(f"faktorial dari", angka, "tersebut adalah", hasil_faktorial)