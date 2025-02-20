import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def predictive_analysis(data_path, model_output_path):
    # Membaca dataset
    data = pd.read_csv(data_path)

    # Pastikan kolom dengan tanggal diubah ke format numerik
    # Misalnya kolom 'Start Date' dan 'End Date' yang berisi tanggal
    data['Start_Date'] = pd.to_datetime(data['Start_Date'], errors='coerce')
    data['Finish_Date'] = pd.to_datetime(data['Finish_Date'], errors='coerce')

    # Menghitung selisih waktu dalam hari dari tanggal referensi (misalnya tanggal proyek dimulai)
    reference_date = pd.to_datetime('2025-01-01')  # Menggunakan tanggal tertentu sebagai referensi
    data['Start Date'] = (data['Start_Date'] - reference_date).dt.days
    data['End Date Days'] = (data['Finish_Date'] - reference_date).dt.days

    # Menghapus kolom yang tidak diperlukan (seperti tanggal dalam format asli)
    data = data.drop(columns=['Start_Date', 'Finish_Date'])

    # Pisahkan fitur dan target
    X = data.drop(columns=['Duration'])  # Fitur yang digunakan untuk prediksi
    y = data['Duration']  # Target (kolom yang ingin diprediksi)

    # Pisahkan data untuk pelatihan dan pengujian
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Inisialisasi model
    model = RandomForestRegressor(random_state=42)

    # Latih model
    model.fit(X_train, y_train)

    # Simpan model ke file
    joblib.dump(model, model_output_path)

    # Mengembalikan skor prediksi
    score = model.score(X_test, y_test)
    return score

# Contoh penggunaan
score = predictive_analysis("../data/cleaned_project_tasks.csv", "../outputs/model.pkl")
print(f"Model R-squared: {score}")
