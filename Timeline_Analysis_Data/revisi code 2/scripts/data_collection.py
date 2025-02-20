# scripts/data_collection.py
import pandas as pd
import os

# Path ke file data
input_file_path = 'D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 2/data/project_schedule.csv'
output_file_path = 'D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 2/outputs/collected_data.csv'

# Membaca data
df = pd.read_csv(input_file_path)

# Menampilkan 5 baris pertama
print("Preview Data:")
print(df.head())

# Simpan data ke folder outputs
os.makedirs('../outputs', exist_ok=True)  # Membuat folder jika belum ada
df.to_csv(output_file_path, index=False)
print(f"Data telah disimpan ke: {output_file_path}")
