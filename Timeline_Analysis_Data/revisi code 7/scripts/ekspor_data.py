from mpxj.reader import UniversalProjectReader
import csv

# Path file Microsoft Project (.mpp)
input_file = 'project_data.mpp'
output_file = 'project_data_export.csv'

# Membaca file .mpp menggunakan MPXJ
reader = UniversalProjectReader()
project = reader.read(input_file)

# Menyusun data dari file Microsoft Project
data = []
headers = ['Task Name', 'Duration', 'Start Date', 'Finish Date']

for task in project.tasks:
    if task is not None:
        data.append([
            task.Name, 
            str(task.Duration), 
            task.Start, 
            task.Finish
        ])

# Menyimpan data ke file CSV
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Menulis header
    writer.writerows(data)   # Menulis data

print(f"Data berhasil diekspor ke {output_file}")
