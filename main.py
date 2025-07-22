import customtkinter as ctk
from customtkinter import *

# Inisialisasi tampilan
set_appearance_mode("light")
set_default_color_theme("green")  # Tema umum (blue, green, dark-blue, etc.)

app = ctk.CTk()  # CTk() adalah pengganti Tk() dari tkinter
app.title("Medication Reminder")
app.geometry("400x400")

# Label Judul
judul_label = ctk.CTkLabel(app, text="Medication Reminder", font=("Poppins", 20))
judul_label.pack(pady=20)

# Tombol Tambah Obat
tambah_btn = ctk.CTkButton(app, text="Tambah Obat", command=lambda: print("Tambah ditekan"))
tambah_btn.pack(pady=10)

# Tombol Lihat Daftar Obat
lihat_btn = ctk.CTkButton(app, text="Lihat Daftar Obat", command=lambda: print("Lihat ditekan"))
lihat_btn.pack(pady=10)

app.mainloop()