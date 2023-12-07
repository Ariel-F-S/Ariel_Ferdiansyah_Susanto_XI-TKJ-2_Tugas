# Nama      : Ariel Ferdiansyah Susanto
# Kelas     : XI-TKJ 2
# No. Absen : 04

# Soal : Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari jumlah apel yang tersisa. Buatlah program yang menghitung berapa hari yang dibutuhkan agar sisa apel kurang dari 20 buah.

apel_awal = 100
dijual = 0.1
target_sisa = 20
hari = 0

while apel_awal >= target_sisa:
    penjualan = apel_awal * dijual
    apel_awal -= penjualan
    hari += 1

print(f"Waktu yang dibutuhkan untuk menjual apel agar tersisa {target_sisa} adalah {hari} hari.")