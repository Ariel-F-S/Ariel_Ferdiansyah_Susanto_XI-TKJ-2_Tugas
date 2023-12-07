# Nama : Ariel Ferdiansyah Susanto
# Kelas : XI-TKJ 2
# N0. Absen : 04
# Soal : Buat program Python yang mengambil data penjualan bulanan produk dan menentukan kategori produk

penjualan = float(input("berhasil terjual = "))

if penjualan >1000:
    print("Produk Terlaris")
elif penjualan >=500:
    print("Produk Populer")
else:
    print("Produk Biasa")
    