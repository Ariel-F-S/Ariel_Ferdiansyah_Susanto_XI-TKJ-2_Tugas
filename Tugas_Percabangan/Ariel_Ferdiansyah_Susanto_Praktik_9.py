# Nama : Ariel Ferdiansyah Susanto
# Kelas : XI-TKJ 2
# N0. Absen : 04
# Soal : Buat program Python yang mengambil status persiapan proyek dan menentukan apakah proyek tersebut dapat diluncurkan. Jika status persiapan "Siap," program harus mencetak "Proyek diluncurkan." Jika status persiapan "Tunda," program harus mencetak "Proyek ditunda."

status_persiapan = input("Apakah persiapan proyek sudah siap? ") #Siap atau Tunda

if status_persiapan.lower() == "siap":
    print("Proyek diluncurkan")
else:
    print("Proyek ditunda")