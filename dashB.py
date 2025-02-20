import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np

# Sample Data
data = {
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'],
    'Penjualan': [23, 17, 35, 29, 42, 38],
    'Pengeluaran': [15, 12, 20, 18, 25, 22]
}

df = pd.DataFrame(data)

# Fungsi untuk update grafik
def update_graph():
    bulan = combo_bulan.get()
    if bulan == "Semua":
        filtered_df = df
    else:
        filtered_df = df[df['Bulan'] == bulan]
    
    ax.clear()
    ax.bar(filtered_df['Bulan'], filtered_df['Penjualan'], color='skyblue', label='Penjualan')
    ax.bar(filtered_df['Bulan'], filtered_df['Pengeluaran'], color='lightgreen', label='Pengeluaran', alpha=0.7)
    ax.set_title('Penjualan dan Pengeluaran')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah')
    ax.legend()
    canvas.draw()

# Membuat window
root = tk.Tk()
root.title("Dashboard Penjualan")
root.geometry("800x600")

# Frame untuk kontrol
control_frame = ttk.Frame(root)
control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# Dropdown untuk memilih bulan
ttk.Label(control_frame, text="Pilih Bulan:").grid(row=0, column=0, padx=5, pady=5)
combo_bulan = ttk.Combobox(control_frame, values=["Semua"] + list(df['Bulan']))
combo_bulan.grid(row=0, column=1, padx=5, pady=5)
combo_bulan.current(0)

# Tombol untuk update grafik
ttk.Button(control_frame, text="Update Grafik", command=update_graph).grid(row=0, column=2, padx=5, pady=5)

# Frame untuk grafik
graph_frame = ttk.Frame(root)
graph_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Membuat grafik
fig, ax = plt.subplots(figsize=(8, 4))
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Menjalankan aplikasi
update_graph()  # Menampilkan grafik awal
root.mainloop()
