# Nama : Ariel Ferdiansyah Susanto
# Kelas : XI-TKJ 2
# N0. Absen : 04
# Soal : Buat program Python yang mengambil informasi pembaruan perangkat lunak dan menentukan apakah sistem perlu di-restart. Jika pembaruan mengharuskan restart, program harus mencetak "Sistem perlu di-restart." Jika tidak, program harus mencetak "Sistem tidak perlu di-restart."

pembaruan = input("Apakah pembaruan perangkat tersedia? ") #iya atau tidak

if pembaruan.lower() == "iya":
    print("Sistem perlu di-restart")
else:
    print("Sistem tidak perlu di-restart")