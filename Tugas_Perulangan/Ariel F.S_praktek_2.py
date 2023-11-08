# Nama      : Ariel Ferdiansyah Susanto
# Kelas     : XI-TKJ 2
# No. Absen : 04

# Soal : Seorang pelari ingin meningkatkan jarak tempuhnya setiap minggunya. Ia mulai dengan 5 kilometer dan meningkatkan jaraknya sebesar 10% setiap minggunya. Buatlah program yang menghitung berapa minggu yang dibutuhkan agar pelari itu dapat berlari lebih dari 10 kilometer.

start = 5
naik_per_minggu = 0.1
target = 10
minggu = 0

while start <= target:
    penjumlahan = start * naik_per_minggu
    start += penjumlahan
    minggu += 1

print(f"Waktu yang dibutuhkan adalah {minggu} minggu")