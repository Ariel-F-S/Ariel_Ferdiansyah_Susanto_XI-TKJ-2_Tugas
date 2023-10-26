# Nama : Ariel Ferdiansyah Susanto
# Kelas : XI-TKJ 2
# N0. Absen : 04
# Soal : Buat program Python yang memeriksa apakah suatu file sudah ada di direktori server. Jika file sudah ada, program harus mencetak "File sudah ada," jika tidak, program harus mencetak "File belum ada."

nama_file ="data.txt"
daftar_file_di_server = ["file1.txt", "file2.txt", "data.txt", "file3.txt"]

if nama_file in daftar_file_di_server:
    print("File Sudah Ada")
else:
    print("File Belum Ada")