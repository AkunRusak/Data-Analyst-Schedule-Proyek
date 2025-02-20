import pandas as pd

def predictive_analysis(data):
    # Menghitung rata-rata durasi task
    avg_duration = data['Duration'].mean()
    
    # Memprediksi tanggal selesai proyek (dengan rata-rata durasi per task)
    predicted_end_date = data['Start_Date'].min() + pd.to_timedelta(avg_duration * len(data), unit='D')
    
    print(f"Durasi rata-rata per task: {avg_duration:.2f} hari")
    print(f"Prediksi tanggal selesai proyek: {predicted_end_date}")
