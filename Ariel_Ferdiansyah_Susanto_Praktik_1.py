# Nama : Ariel Ferdiansyah Susanto
# Kelas : XI-TKJ 2
# N0. Absen : 04
# Soal : Buat program Python yang mengambil total belanjaan pelanggan dan memberikan diskon

total_belanjaan = float(input("Total belanjaan Anda: "))

if total_belanjaan > 500000:
    diskon = total_belanjaan * 0.10
elif total_belanjaan >= 300000:
    diskon = total_belanjaan * 0.05
else:
    diskon = 0

total_pembayaran = total_belanjaan - diskon
print(f"Total pembayaran setelah diskon: {total_pembayaran}")