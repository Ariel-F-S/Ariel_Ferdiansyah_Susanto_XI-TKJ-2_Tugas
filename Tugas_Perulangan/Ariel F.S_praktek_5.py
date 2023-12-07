# Nama      : Ariel Ferdiansyah Susanto
# Kelas     : XI-TKJ 2
# No. Absen : 04

# Soal : Sebuah bakteri pembelahan setiap 20 menit. Sebuah bakteri ditempatkan dalam lingkungan yang cocok dan berkembang biak dengan cepat. Buatlah program yang menghitung berapa kali pembelahan bakteri terjadi dalam rentang waktu 2 jam.

waktu_membelah = 20
waktu = 120
awal = 0

while waktu >= waktu_membelah:
    waktu -= waktu_membelah
    awal += 1

print(f"Dalam waktu dua jam maka bakteri bisa membelah diri sebanyak {awal} kali")