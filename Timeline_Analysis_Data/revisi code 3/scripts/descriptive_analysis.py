# scripts/descriptive_analysis.py
import pandas as pd

# Path ke file input dan output
input_file_path = 'D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 3/outputs/data_cleaning/cleaned_data.csv'
output_file_path = 'D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 3/outputs/descriptive_analysis/descriptive_analysis.txt'

# Membaca data
df = pd.read_csv(input_file_path)

def descriptive_analysis(dataframe):
    # Statistik deskriptif
    stats = dataframe.describe()
    
    # Jumlah tugas per WBS
    task_per_wbs = dataframe['WBS'].value_counts()
    
    # Simpan ke file CSV
    stats.to_csv("D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 3/outputs/descriptive_analysis/descriptive_stats.csv")
    task_per_wbs.to_csv("D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 3/outputs/descriptive_analysis/tasks_per_wbs.csv", header=["Task Count"])
    
    return stats, task_per_wbs

stats, task_per_wbs = descriptive_analysis(df)
