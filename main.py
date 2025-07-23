import customtkinter as ctk
from tkinter import messagebox

obat_list = []

def open_lihat_obat():
    if not obat_list:
        messagebox.showinfo("Info", "Belum ada reminder obat yang disimpan.")
        return

    lihat_window = ctk.CTkToplevel(app)
    lihat_window.title("Daftar Reminder Obat")
    lihat_window.geometry("350x300")

    label = ctk.CTkLabel(lihat_window, text="Reminder Obat", font=ctk.CTkFont(size=16, weight="bold"))
    label.pack(pady=10)

    for idx, obat in enumerate(obat_list, start=1):
        info = f"{idx}. {obat['nama']} - {obat['tanggal']} jam {obat['waktu']}"
        label_obat = ctk.CTkLabel(lihat_window, text=info)
        label_obat.pack(anchor="w", padx=15, pady=2)


def open_tambah_obat():
    tambah_window = ctk.CTkToplevel(app)
    tambah_window.title("Tambah Obat")
    tambah_window.geometry("300x300")

    label_nama = ctk.CTkLabel(tambah_window, text="Nama Obat:")
    label_nama.pack(pady=5)
    entry_nama = ctk.CTkEntry(tambah_window)
    entry_nama.pack(pady=5)

    label_tanggal = ctk.CTkLabel(tambah_window, text="Tanggal Minum (DD-MM-YYYY):")
    label_tanggal.pack(pady=5)
    entry_tanggal = ctk.CTkEntry(tambah_window)
    entry_tanggal.pack(pady=5)

    label_waktu = ctk.CTkLabel(tambah_window, text="Waktu Minum (HH:MM):")
    label_waktu.pack(pady=5)
    entry_waktu = ctk.CTkEntry(tambah_window)
    entry_waktu.pack(pady=5)

    def simpan_obat():
        nama = entry_nama.get()
        tanggal = entry_tanggal.get()
        waktu = entry_waktu.get()

        if not nama or not tanggal or not waktu:
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return
        
        # Simpan data ke list sementara
        obat_list.append({
            "nama": nama,
            "tanggal": tanggal,
            "waktu": waktu
        })

        messagebox.showinfo("Berhasil", f"Obat '{nama}' berhasil disimpan!")
        tambah_window.destroy()

    simpan_btn = ctk.CTkButton(tambah_window, text="Simpan", command=simpan_obat)
    simpan_btn.pack(pady=15)

# --- Main Window ---
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Reminder Obat")
app.geometry("400x300")

label = ctk.CTkLabel(app, text="Aplikasi Reminder Obat", font=ctk.CTkFont(size=20, weight="bold"))
label.pack(pady=20)

btn_tambah = ctk.CTkButton(app, text="Tambah Obat", command=open_tambah_obat)
btn_tambah.pack(pady=10)

btn_lihat = ctk.CTkButton(app, text="Lihat Daftar Obat", command=open_lihat_obat)
btn_lihat.pack(pady=10)

app.mainloop()