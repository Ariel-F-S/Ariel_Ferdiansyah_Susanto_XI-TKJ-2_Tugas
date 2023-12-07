# Nama : Ariel Ferdiansyah Susanto
# Kelas : XI-TKJ 2
# N0. Absen : 04
# Soal : Buat program Python yang mengambil nilai tugas (skala 0-100) dan nilai ujian (skala 0-100) seorang siswa dan menentukan nilai akhirnya. Jika nilai tugas lebih dari 70 dan nilai ujian lebih dari 60, siswa lulus dengan nilai "Lulus". Jika tidak, siswa gagal dengan nilai "Gagal".


nilai_tugas = float(input("Nilai Tugas skala 0-100")) 
nilai_ujian = float(input("Nilai Ujian skala 0-100"))

if nilai_tugas >70 and nilai_ujian >60:
    print("Lulus")
else:
    print("Gagal")