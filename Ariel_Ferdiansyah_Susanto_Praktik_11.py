# Nama : Ariel Ferdiansyah Susanto
# Kelas : XI-TKJ 2
# N0. Absen : 04
# Soal : Buat program Python yang mengambil nilai performa karyawan (1 hingga 5, dengan 5 sebagai performa terbaik) dan menghitung bonus tahunan

peforma = float(input("Masukkan peforma karyawan Anda (dari 1-5): ")) #kategori 1-5
gaji = float(input("Gaji Karyawan dalam setahun: "))

if peforma == 5:
    bonus = gaji * 0.20
elif peforma == 4:
    bonus = gaji * 0.10
elif peforma == 3:
    bonus = gaji * 0.05
elif peforma == 2:
    bonus = gaji * 0.02
else:
    bonus = 0

total_gaji = bonus + gaji
print(f"Total gaji tahunan karyawan: {total_gaji}")