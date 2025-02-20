import pandas as pd
from datetime import datetime

def clean_data(file_path):
    # Membaca data dari file CSV
    data = pd.read_csv(file_path='D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 7/data/project_data.csv')
    
    # Menghapus spasi di kolom
    data.columns = data.columns.str.strip()
    
    # Mengubah kolom tanggal ke format datetime
    data['Start_Date'] = pd.to_datetime(data['Start_Date'], format='%d %B %Y %H.%M', errors='coerce')
    data['Finish_Date'] = pd.to_datetime(data['Finish_Date'], format='%d %B %Y %H.%M', errors='coerce')
    
    # Memastikan kolom Duration dalam bentuk angka
    data['Duration'] = data['Duration'].str.extract(r'(\d+)').astype(float)
    
    # Menghapus baris dengan nilai NaN
    data = data.dropna()
    data.to_csv('D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 7/outputs/clean_project_data.csv', index=False)


