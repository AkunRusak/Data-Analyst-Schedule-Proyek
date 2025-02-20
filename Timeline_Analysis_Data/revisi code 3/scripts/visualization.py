# scripts/visualization.py
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import os
from sklearn.preprocessing import LabelEncoder

# Membuat folder output untuk visualisasi
visualization_path = 'D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 3/outputs/visualizations/'
os.makedirs(visualization_path, exist_ok=True)

# Membaca data yang telah dibersihkan
input_file_path = 'D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 3/outputs/predictive_analysis/prediction_results.csv'
df = pd.read_csv(input_file_path)

# Memastikan kolom tanggal memiliki format datetime
df['Start_Date'] = pd.to_datetime(df['Start_Date'])
df['Finish_Date'] = pd.to_datetime(df['Finish_Date'])

# Menambahkan kolom Duration jika belum ada
if 'Duration' not in df.columns:
    df['Duration'] = (df['Finish_Date'] - df['Start_Date']).dt.days

# Menampilkan preview data untuk memastikan format data
print("Preview Data:")
print(df.head())

# 1. Histogram untuk Distribusi Durasi
plt.figure(figsize=(8, 6))  # Ukuran grafik
plt.hist(df['Duration'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.title('Distribusi Durasi Tugas', fontsize=16)
plt.xlabel('Durasi (hari)', fontsize=12)
plt.ylabel('Frekuensi', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Garis grid horizontal
plt.savefig(os.path.join(visualization_path, 'duration_distribution.png'))
plt.close()
print(f"Histogram distribusi durasi telah disimpan di: {visualization_path}duration_distribution.png")

# 2. Scatter Plot: Hubungan Start_Date dan Durasi
# Mengubah Start_Date menjadi tipe datetime untuk digunakan dalam plot
df['Start_Date'] = pd.to_datetime(df['Start_Date'])

plt.figure(figsize=(10, 6))
plt.scatter(df['Start_Date'], df['Duration'], color='purple', alpha=0.7)
plt.title('Hubungan Tanggal Mulai dan Durasi Tugas', fontsize=16)
plt.xlabel('Tanggal Mulai', fontsize=12)
plt.ylabel('Durasi (hari)', fontsize=12)
plt.xticks(rotation=45)  # Rotasi label pada sumbu x
plt.grid(linestyle='--', alpha=0.5)
plt.savefig(os.path.join(visualization_path, 'start_date_vs_duration.png'))
plt.close()
print(f"Scatter plot hubungan Tanggal Mulai dan Durasi telah disimpan di: {visualization_path}start_date_vs_duration.png")

# 3. Bar Plot: Jumlah Tugas per Bulan Mulai
# Konversi kolom Start_Date ke datetime jika belum dalam format datetime
df['Start_Date'] = pd.to_datetime(df['Start_Date'])

# Membuat kolom tambahan untuk Tahun dan Bulan
df['Start_YearMonth'] = df['Start_Date'].dt.to_period('M')  # Format Year-Month (YYYY-MM)

# Menghitung jumlah tugas per bulan
tasks_per_month = df['Start_YearMonth'].value_counts().sort_index()

# Membuat bar plot
plt.figure(figsize=(12, 6))
tasks_per_month.plot(kind='bar', color='blue', alpha=0.7, edgecolor='black')
plt.title('Jumlah Tugas per Bulan', fontsize=16)
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Jumlah Tugas', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Pastikan direktori visualisasi ada
os.makedirs(visualization_path, exist_ok=True)

# Simpan plot ke file
plt.savefig(os.path.join(visualization_path, 'tasks_per_month.png'))
plt.close()
print(f"Bar plot jumlah tugas per bulan telah disimpan di: {visualization_path}tasks_per_month.png")

# 4. Correlation Heatmap
# Memastikan kolom 'Name' ada dalam dataframe
if 'Name' in df.columns:
    # Encode kolom string menjadi numerik menggunakan LabelEncoder
    categorical_columns = ['Task_Encoded']  # Tentukan kolom yang ingin di-encode
    label_encoders = {}
    for col in categorical_columns:
        le = LabelEncoder()
        df[col + "_encoded"] = le.fit_transform(df[col].astype(str))  # Pastikan data dalam bentuk string
        label_encoders[col] = le

    # Gabungkan semua kolom untuk analisis korelasi
    numerical_columns = df.select_dtypes(include=['number']).columns
    columns_for_correlation = list(numerical_columns) + [col + "_encoded" for col in categorical_columns]
    correlation_matrix = df[columns_for_correlation].corr()

    # Plot heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
    plt.title('Correlation Heatmap (Numerical and Encoded Categorical)', fontsize=16)

    # Simpan visualisasi
    output_file = os.path.join(visualization_path, 'correlation_heatmap_encoded.png')
    plt.savefig(output_file)
    plt.close()
    print(f"Heatmap korelasi telah disimpan di: {output_file}")
else:
    print("Kolom 'Name' tidak ditemukan dalam DataFrame.")

# 5. Line Plot: Tren Durasi Berdasarkan Tanggal Mulai
# Menyortir data berdasarkan Start_Date
df = df.sort_values(by='Start_Date')

plt.figure(figsize=(10, 6))
plt.plot(df['Start_Date'], df['Duration'], marker='o', color='orange', alpha=0.7)
plt.title('Tren Durasi Tugas Berdasarkan Tanggal Mulai', fontsize=16)
plt.xlabel('Tanggal Mulai', fontsize=12)
plt.ylabel('Durasi (hari)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(linestyle='--', alpha=0.5)
plt.savefig(os.path.join(visualization_path, 'duration_trend.png'))
plt.close()
print(f"Line plot tren durasi berdasarkan tanggal mulai telah disimpan di: {visualization_path}duration_trend.png")


