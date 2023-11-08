# Nama      : Ariel Ferdiansyah Susanto
# Kelas     : XI-TKJ 2
# No. Absen : 04

# Soal : Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap tahunnya. Buatlah program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi melebihi 20.000 dollar.

awal = 100000
target = 200000
per_tahun = 0.06
tahun = 0

while awal <= target:
   penjumlahan = awal * per_tahun
   awal += penjumlahan
   tahun += 1

print(f"Waktu yang dibutuhkan untuk mencapai {target} adalah {tahun} tahun")