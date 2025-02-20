# Import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import os

# Path ke file input dan output
input_file_path = 'D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 3/outputs/data_cleaning/cleaned_data.csv'
output_csv_path = 'D:/Kampus/OnProggress/Kerja Praktek/Timeline_Analysis_Data/revisi code 3/outputs/predictive_analysis/prediction_results.csv'

# Membaca data
df = pd.read_csv(input_file_path)

# Tambahkan kolom WBS jika belum ada
if 'WBS' not in df.columns:
    df['WBS'] = ['WBS-' + str(i + 1) for i in range(len(df))]

# Urutkan data berdasarkan kolom WBS
df = df.sort_values(by='WBS')

# Encode kolom WBS dan Task Name sebagai fitur numerik
df['WBS_Encoded'] = df['WBS'].str.extract('(\d+)').astype(int)  # Ekstrak angka dari WBS
df['Task_Encoded'] = df['Name'].astype('category').cat.codes  # Encode Task Name

# Fitur (X) dan target (y)
X = df[['WBS_Encoded', 'Task_Encoded']]
y = df['Duration']

# Bagi data menjadi set pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Melatih model regresi linier
model = LinearRegression()
model.fit(X_train, y_train)

# Menampilkan koefisien dan intercept
print("Koefisien model:", model.coef_)
print("Intercept model:", model.intercept_)

# Membuat prediksi pada data uji
y_pred = model.predict(X_test)

# Membuat prediksi pada data uji
y_pred = model.predict(X_test)

# Prediksi pada data pengujian
df['Predicted_Duration'] = model.predict(X)

# Simpan hasil prediksi ke file CSV
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
df.to_csv(output_csv_path, index=False)

print(f"Hasil prediksi telah disimpan ke: {output_csv_path}")

# Evaluasi model
from sklearn.metrics import r2_score

# Hitung R-squared dan Regressi
r2 = r2_score(y_test, model.predict(X_test))

print(f"R-squared: {r2:.2f}")
print("Prediksi:", y_pred)
