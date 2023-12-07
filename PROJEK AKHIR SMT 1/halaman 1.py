import tkinter as tk
from PIL import Image, ImageTk

def create_boxes():
    for row in range(5):
        for col in range(5):
            # Baca file gambar (ganti 'path_to_your_image.png' dengan path gambar yang Anda miliki)
            try:
                image = Image.open('path_to_your_image.png')
                image = image.resize((100, 100), Image.ANTIALIAS)  # Sesuaikan ukuran gambar sesuai kebutuhan
                photo = ImageTk.PhotoImage(image)
            except FileNotFoundError:
                print("File gambar tidak ditemukan.")

            box = tk.Label(frame, image=photo, borderwidth=2, relief='solid', width=100, height=100)
            box.photo = photo  # Simpan referensi agar gambar tidak dihapus oleh garbage collector
            box.grid(row=row, column=col, padx=5, pady=5)

# Membuat jendela utama
root = tk.Tk()
root.title("Desktop dengan Kotak Foto")

# Membuat dan menempatkan elemen-elemen di dalam jendela
frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

# Membuat kotak-kotak dengan foto
create_boxes()

# Menjalankan loop utama
root.mainloop()
