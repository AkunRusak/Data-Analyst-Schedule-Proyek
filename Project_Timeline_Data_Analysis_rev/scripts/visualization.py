import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_clean = pd.read_csv('D:/Kampus/OnProggress/Kerja Praktek/Project_Timeline_Data_Analysis/outputs/clean_project_data.csv')
sns.scatterplot(x='Task_Duration', y='Project_Delay', data=data_clean)
plt.title('Hubungan Durasi Tugas dengan Keterlambatan Proyek')
plt.xlabel('Durasi Tugas (hari)')
plt.ylabel('Keterlambatan Proyek (hari)')
plt.show()
