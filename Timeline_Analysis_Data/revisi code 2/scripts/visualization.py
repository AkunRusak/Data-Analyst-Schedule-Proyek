# scripts/visualization.py
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import os

# Membuat folder output untuk visualisasi
visualization_path = 'D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 2/outputs/visualizations/'
os.makedirs(visualization_path, exist_ok=True)

# Membaca data yang telah dibersihkan
input_file_path = 'D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 2/outputs/cleaned_data.csv'
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

# 3. Bar Plot: Jumlah Tugas per Tahun Mulai
# Membuat kolom tambahan untuk tahun dari Start_Date
df['Start_Year'] = df['Start_Date'].dt.year

plt.figure(figsize=(8, 6))
task_per_year = df['Start_Year'].value_counts().sort_index()  # Menghitung tugas per tahun
task_per_year.plot(kind='bar', color='green', alpha=0.7, edgecolor='black')
plt.title('Jumlah Tugas per Tahun Mulai', fontsize=16)
plt.xlabel('Tahun Mulai', fontsize=12)
plt.ylabel('Jumlah Tugas', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(os.path.join(visualization_path, 'tasks_per_year.png'))
plt.close()
print(f"Bar plot jumlah tugas per tahun telah disimpan di: {visualization_path}tasks_per_year.png")

# 4. Correlation Heatmap
# Menampilkan korelasi antara kolom numerik
plt.figure(figsize=(8, 6))
correlation_matrix = df[['Duration']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', cbar=True)
plt.title('Correlation Heatmap', fontsize=16)
plt.savefig(os.path.join(visualization_path, 'correlation_heatmap.png'))
plt.close()
print(f"Heatmap korelasi telah disimpan di: {visualization_path}correlation_heatmap.png")

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


# 6. Gantt Chart
# Membuat Gantt Chart menggunakan Plotly
fig = px.timeline(
    df,
    x_start="Start_Date",
    x_end="Finish_Date",
    y="Task Name",
    title="Gantt Chart Proyek",
    labels={"Task Name": "Nama Tugas", "Start_Date": "Tanggal Mulai", "Finish_Date": "Tanggal Selesai"},
    color="Duration",  # Menggunakan durasi sebagai pembeda warna
    template="plotly_white",  # Template desain bersih
)

# Menyesuaikan layout agar menyerupai MS Project
fig.update_layout(
    xaxis_title="Tanggal",
    yaxis_title="Tugas",
    yaxis=dict(autorange="reversed"),  # Membalikkan urutan tugas seperti MS Project
    title=dict(font=dict(size=20), x=0.5),  # Pusatkan judul
    xaxis=dict(showgrid=True),  # Menampilkan grid
    height=600,  # Menyesuaikan tinggi chart
)

# Menyimpan Gantt Chart sebagai file HTML interaktif
output_file_path = os.path.join(visualization_path, 'gantt_chart.html')
fig.write_html(output_file_path)
print(f"Gantt Chart telah disimpan di: {output_file_path}")

# Menampilkan Gantt Chart di browser (opsional)
fig.show()