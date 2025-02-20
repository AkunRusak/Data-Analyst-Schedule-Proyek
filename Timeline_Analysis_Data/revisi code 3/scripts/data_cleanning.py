# scripts/data_cleaning.py
import pandas as pd
import os

# Path ke file input dan output
input_file_path = 'D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 3/outputs/data_collection/collected_data.csv'
output_file_path = 'D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 3/outputs/data_cleaning/cleaned_data.csv'

# Membaca data
df = pd.read_csv(input_file_path)

# Membersihkan data (contoh: menghapus nilai kosong dan konversi tipe data)
df.dropna(inplace=True)  # Menghapus baris dengan nilai kosong
df['Duration'] = df['Duration'].str.replace(' days', '').str.replace(' day', '').astype(int)  # Konversi ke numeric
df['Start_Date'] = pd.to_datetime(df['Start_Date'], format="%d %B %Y %H.%M")  # Konversi ke datetime
df['Finish_Date'] = pd.to_datetime(df['Finish_Date'], format="%d %B %Y %H.%M")  # Konversi ke datetime

# Simpan data yang telah dibersihkan
df.to_csv(output_file_path, index=False)
print(f"Data telah dibersihkan dan disimpan ke: {output_file_path}")
