<<<<<<< HEAD
# Nama : Ariel Ferdiansyah Susanto
# Kelas : XI-TKJ 2
# N0. Absen : 04
# Soal : Buat program Python yang mengambil total belanjaan dan status anggota (biasa atau premium).

member = (input("Apakah memiliki member premium?")) #isi ya atau tidak
total_belanja = float(input("masukkan total belanja"))

if member.lower() == "iya":
    if total_belanja > 500000:
        diskon = total_belanja * 0.15 
    else:
        diskon = total_belanja * 0.10
elif member.lower() == "tidak":
    if total_belanja > 300000:
        diskon =total_belanja * 0.7
    else:
        diskon = total_belanja * 0
else:
    diskon = 0

total_pembayaran = total_belanja - diskon
=======
# Nama : Ariel Ferdiansyah Susanto
# Kelas : XI-TKJ 2
# N0. Absen : 04
# Soal : Buat program Python yang mengambil total belanjaan dan status anggota (biasa atau premium).

member = (input("Apakah memiliki member premium?")) #isi ya atau tidak
total_belanja = float(input("masukkan total belanja"))

if member.lower() == "iya":
    if total_belanja > 500000:
        diskon = total_belanja * 0.15 
    else:
        diskon = total_belanja * 0.10
elif member.lower() == "tidak":
    if total_belanja > 300000:
        diskon =total_belanja * 0.7
    else:
        diskon = total_belanja * 0
else:
    diskon = 0

total_pembayaran = total_belanja - diskon
>>>>>>> c326b4335814a81d3d652480bc133b6024bcdd27
print(f"total pembayaran setelah diskon: {total_pembayaran}")