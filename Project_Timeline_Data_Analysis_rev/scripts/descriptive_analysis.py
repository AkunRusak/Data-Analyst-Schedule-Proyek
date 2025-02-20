import pandas as pd
import matplotlib.pyplot as plt
data_clean = pd.read_csv('D:/Kampus/OnProggress/Kerja Praktek/Project_Timeline_Data_Analysis/outputs/clean_project_data.csv')
plt.hist(data_clean['Task_Duration'], bins=20, edgecolor='black')
plt.title('Distribusi Durasi Tugas Proyek')
plt.xlabel('Durasi (hari)')
plt.ylabel('Frekuensi')
plt.show()
