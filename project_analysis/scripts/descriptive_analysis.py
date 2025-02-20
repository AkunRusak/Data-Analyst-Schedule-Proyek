import pandas as pd
import json

def analyze_data(input_path, output_path):
    # Membaca data yang sudah dibersihkan
    data = pd.read_csv(input_path)

    # Lakukan analisis deskriptif atau statistik pada data
    descriptive_stats = data.describe()

    # Pastikan semua nilai numerik adalah tipe int yang bisa diserialisasi ke JSON
    descriptive_stats = descriptive_stats.applymap(lambda x: int(x) if isinstance(x, pd.Timestamp) else x)

    # Menyimpan hasil analisis ke file JSON
    with open(output_path, "w") as f:
        json.dump(descriptive_stats.to_dict(), f, indent=4)

    print(f"Descriptive stats telah disimpan di {output_path}")
