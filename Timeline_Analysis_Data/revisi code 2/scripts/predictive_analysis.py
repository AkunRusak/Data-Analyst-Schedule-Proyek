# scripts/predictive_analysis.py
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os

# Path ke file input dan output
input_file_path = 'D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 2/outputs/cleaned_data.csv'
output_model_path = 'D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 2/outputs/predictive_model.pkl'

# Membaca data
df = pd.read_csv(input_file_path)

# Memastikan kolom tidak memiliki NaN
print("Sebelum membersihkan NaN pada kolom Duration:")
print(df['Duration'].isna().sum())  # Tampilkan jumlah nilai NaN di kolom Duration

# Hapus baris dengan nilai NaN di kolom Duration
df = df.dropna(subset=['Duration'])

# Memastikan nilai NaN sudah dibersihkan
print("Setelah membersihkan NaN pada kolom Duration:")
print(df['Duration'].isna().sum())  # Harus 0

# Tambahkan kolom baru Days_From_Start
df['Days_From_Start'] = (pd.to_datetime(df['Start_Date']) - pd.to_datetime("2000-01-01")).dt.days

# Persiapkan data untuk model
X = df[['Days_From_Start']]
y = df['Duration']

# Melatih model
model = LinearRegression()
model.fit(X, y)

# Simpan model
import pickle
os.makedirs('../outputs', exist_ok=True)
with open(output_model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"Model prediktif telah disimpan ke: {output_model_path}")
