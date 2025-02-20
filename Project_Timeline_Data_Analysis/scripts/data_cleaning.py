import pandas as pd
data = pd.read_csv('D:/Kampus/OnProggress/Kerja Praktek/Project_Timeline_Data_Analysis/data/project_data.csv')
data_clean = data.dropna()
# data_clean['start_date'] = pd.to_datetime(data_clean['start_date'])
data_clean['Start_Date'] = pd.to_datetime(data_clean['Start_Date'])
data_clean['End_Date'] = pd.to_datetime(data_clean['End_Date'])
data_clean.to_csv('D:/Kampus/OnProggress/Kerja Praktek/Project_Timeline_Data_Analysis/outputs/clean_project_data.csv', index=False)
