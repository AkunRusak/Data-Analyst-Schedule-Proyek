# scripts/descriptive_analysis.py
import pandas as pd
import os

# Path ke file input dan output
input_file_path = 'D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 2/outputs/cleaned_data.csv'
output_file_path = 'D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 2/outputs/descriptive_analysis.txt'

# Membaca data
df = pd.read_csv(input_file_path)

# Melakukan analisis deskriptif
description = df.describe()

# Simpan analisis deskriptif ke file teks
os.makedirs('../outputs', exist_ok=True)
with open(output_file_path, 'w') as f:
    f.write("Descriptive Analysis:\n")
    f.write(description.to_string())

print(f"Hasil analisis deskriptif telah disimpan ke: {output_file_path}")
