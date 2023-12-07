from PIL import Image, ImageTk
import tkinter as tk

# Buat jendela tkinter
root = tk.Tk()
root.title("Tampilkan Foto")

# Buka gambar dengan Pillow
image = Image.open("C:/Users/ASUS/Documents/BENGKEL TKJ KLS 11/PEMROGRAMAN/Ariel_Ferdiansyah_Susanto_XI-TKJ-2_Tugas/PROJEK AKHIR SMT 1/FRONT END/1.png")

# Konversi gambar menjadi format yang dapat digunakan oleh tkinter
tk_image = ImageTk.PhotoImage(image)

# Tampilkan gambar di label
label = tk.Label(root, image=tk_image)
label.pack()

# Mulai jendela tkinter
root.mainloop()
