# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error

# data_clean = pd.read_csv('D:/Kampus/OnProggress/Kerja Praktek/Project_Timeline_Data_Analysis/outputs/clean_project_data.csv')
# X = data_clean[['Task_Duration', 'Resource_Alloc']]
# y = data_clean['Project_Delay']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = LinearRegression()
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# print(f'Mean Squared Error: {mse}')


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# membaca dataset
data = pd.read_csv('D:/Kampus/OnProggress/Kerja Praktek/Project_Timeline_Data_Analysis/outputs/clean_project_data.csv')

# pembersihan dan pra-pemrosesan data
data['Start_Date'] = pd.to_datetime(data['Start_Date'])
data['End_Date'] = pd.to_datetime(data['End_Date'])

# menghitung durasi aktual pekerjaan
data['Durasi_Aktual'] = (data['End_Date'] - data['Start_Date']).dt.days

# menghapus kolom yang tidak dibutuhkan
data_clean = data[['Task_Duration', 'Resource_Alloc', 'Durasi_Aktual']]

# memisahkan fitur dan target
X = data_clean[['Task_Duration', 'Resource_Alloc']]  # Fitur: durasi tugas dan sumber daya
y = data_clean['Durasi_Aktual']  # Target: durasi aktual

# memisahkan data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# membuat model regresi linear
model = LinearRegression()

# melatih model
model.fit(X_train, y_train)

# memprediksi hasil berdasarkan data uji
y_pred = model.predict(X_test)

# evaluasi model
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

print("Root Mean Squared Error (RMSE):", rmse)

# menampilkan hasil prediksi dan hasil aktual
hasil = pd.DataFrame({'Prediksi': y_pred, 'Aktual': y_test})
print(hasil)

# menyimpan hasil prediksi ke file CSV
hasil.to_csv('outputs/prediksi_durasi.csv', index=False)
print("Hasil prediksi telah disimpan ke outputs/prediksi_durasi.csv")
