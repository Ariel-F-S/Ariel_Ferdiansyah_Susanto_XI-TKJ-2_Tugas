# Nama : Ariel Ferdiansyah Susanto
# Kelas : XI-TKJ 2
# N0. Absen : 04
# Soal : Buat program Python yang mengambil durasi peminjaman buku dalam hari dan menentukan jenis pinjaman

durasi_pinjam = float(input("Masukkan lama meminjam: ")) 

if durasi_pinjam <= 7:
    print("Peminjaman pendek")
elif durasi_pinjam >30:
    print("Peminjaman panjang")
else:
    print("Peminjaman menengah")
