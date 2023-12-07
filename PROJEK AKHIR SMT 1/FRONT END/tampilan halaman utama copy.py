import tkinter as tk
from tkinter import PhotoImage, filedialog
from PIL import Image, ImageTk

class DesktopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Desktop App")
        
        # Header
        self.header_frame = tk.Frame(self.root, bg="#f0f0f0", height=100)
        self.header_frame.grid(row=0, column=0, columnspan=4, sticky="ew")  

        # Logo
        image = ImageTk.PhotoImage(file="C:/Users/ASUS/Documents/BENGKEL TKJ KLS 11/PEMROGRAMAN/Ariel_Ferdiansyah_Susanto_XI-TKJ-2_Tugas/PROJEK AKHIR SMT 1/FRONT END/1.png")
        original_image = Image.open("C:/Users/ASUS/Documents/BENGKEL TKJ KLS 11/PEMROGRAMAN/Ariel_Ferdiansyah_Susanto_XI-TKJ-2_Tugas/PROJEK AKHIR SMT 1/FRONT END/1.png")
        resized_image = original_image.resize((75, 75))
        self.logo_image = ImageTk.PhotoImage(resized_image)
        self.logo_label = tk.Label(self.header_frame, image=self.logo_image, padx=10)
        self.logo_label.grid(row=0, column=0, padx=(10, 0), pady=5, sticky="w")
        self.logo_label.image = image

        # Judul "My Memories"
        self.title_label = tk.Label(self.header_frame, text="My Memories", fg="black", bg="#f0f0f0")
        self.title_label.grid(row=0, column=1, padx=(0, 10), pady=5, sticky="w")

     # Search Bar
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self.header_frame, textvariable=self.search_var, bg="white", fg="black", insertbackground="white")
        self.search_entry.grid(row=0, column=9, padx=300, pady=20, sticky="e")  # Menggunakan nilai sticky "e" untuk posisi kanan

# Button Search
        self.search_button = tk.Button(self.header_frame, text="Search", command=self.perform_search, bg="#f0f0f0", fg="black")
        self.search_button.grid(row=0, column=10, padx=400, pady=20, sticky="w")  # Menggunakan nilai sticky "w" untuk posisi kiri


        # Isi
        self.frame = tk.Frame(self.root, bg="black")
        self.frame.grid(row=1, column=0, columnspan=4, sticky="nsew")  

        # Kotak 1
        self.box_frame1 = tk.Frame(self.frame, bg="white", width=200, height=200)
        self.box_frame1.grid(row=0, column=1, padx=150, pady=200, sticky="nsew", columnspan=2)  

        # Kotak 2
        self.box_frame2 = tk.Frame(self.frame, bg="white", width=200, height=200)
        self.box_frame2.grid(row=0, column=7, padx=150, pady=200, sticky="nsew", columnspan=2)  

        # Kotak 3
        self.box_frame3 = tk.Frame(self.frame, bg="white", width=200, height=200)
        self.box_frame3.grid(row=0, column=9, padx=150, pady=200, sticky="nsew", columnspan=2)  

        # Tombol tambah gambar
        self.add_button = tk.Button(self.root, text="+", command=self.add_image, font=("Helvetica", 16), width=3, height=1, bg="black", fg="white")
        self.add_button.grid(row=4, column=3, padx=10, pady=10, sticky="se")

        # Mengatur agar kolom dan baris bisa mengekspansi
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(2):
            self.root.grid_rowconfigure(i, weight=1)

    def perform_search(self):
        search_query = self.search_var.get()
        print(f"Performing search for: {search_query}")

    def add_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            try:
                original_image = Image.open(file_path)
                resized_image = original_image.resize((100, 100), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(resized_image)

                # Menambahkan gambar ke frame gambar
                if not hasattr(self, 'image_label1'):
                    self.image_label1 = tk.Label(self.box_frame1, image=photo, bg="white")
                    self.image_label1.image = photo
                    self.image_label1.pack()
                elif not hasattr(self, 'image_label2'):
                    self.image_label2 = tk.Label(self.box_frame2, image=photo, bg="white")
                    self.image_label2.image = photo
                    self.image_label2.pack()
                elif not hasattr(self, 'image_label3'):
                    self.image_label3 = tk.Label(self.box_frame3, image=photo, bg="white")
                    self.image_label3.image = photo
                    self.image_label3.pack()

            except Exception as e:
                print(f"Error loading image: {e}")

        self.total_gambar = PhotoImage(file="ICON IMAGE.png")

if __name__ == "__main__":
    root = tk.Tk()
    app = DesktopApp(root)
    root.mainloop()
