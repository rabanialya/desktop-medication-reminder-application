import customtkinter as ctk

# Inisialisasi tampilan
ctk.set_appearance_mode("System")  # "Dark", "Light", atau "System"
ctk.set_default_color_theme("blue")  # atau "green", "dark-blue"

app = ctk.CTk()  # CTk() adalah pengganti Tk() dari tkinter
app.title("Reminder Obat")
app.geometry("400x300")

# Label Judul
judul_label = ctk.CTkLabel(app, text="Aplikasi Reminder Obat", font=("Arial", 20))
judul_label.pack(pady=20)

# Tombol Tambah Obat
tambah_btn = ctk.CTkButton(app, text="Tambah Obat", command=lambda: print("Tambah ditekan"))
tambah_btn.pack(pady=10)

# Tombol Lihat Daftar Obat
lihat_btn = ctk.CTkButton(app, text="Lihat Daftar Obat", command=lambda: print("Lihat ditekan"))
lihat_btn.pack(pady=10)

app.mainloop()