# Nama : Ariel Ferdiansyah Susanto
# Kelas : XI-TKJ 2
# N0. Absen : 04
# Soal : Buat program Python yang mengambil estimasi waktu selesai proyek dan tanggal target selesai. Jika estimasi waktu selesai lebih awal atau sama dengan tanggal target, program harus mencetak "Tepat waktu," jika tidak, program harus mencetak "Terlambat."

target_proyek = (input("targat-proyek")) #tahun-bulan-hari
estimasi_selesai = (input("estimasi_selesai")) #tahun-bulan-hari

if estimasi_selesai <= target_proyek:
    print("Tepat Waktu")
else:
    print("Terlambat") 