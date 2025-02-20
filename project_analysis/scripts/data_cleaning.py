import pandas as pd

def clean_data(input_path, output_path):
    # Membaca data dari file CSV
    data = pd.read_csv(input_path)

    # Menampilkan beberapa baris pertama untuk memverifikasi data
    print("Data Awal:")
    print(data.head())

    # Coba tentukan format tanggal secara eksplisit
    date_format = "%d %B %Y %H.%M"  # Format yang sesuai dengan data Anda (contoh: "01 January 2025 08.00")
    
    # Parsing tanggal dengan format yang lebih spesifik
    try:
        data['Start_Date'] = pd.to_datetime(data['Start_Date'], format=date_format, errors='raise')
        data['Finish_Date'] = pd.to_datetime(data['Finish_Date'], format=date_format, errors='raise')
    except ValueError as e:
        print(f"Error dalam parsing tanggal: {e}")
        # Jika terjadi kesalahan parsing, bisa memilih untuk menghapus atau menandai data yang rusak
        # Misalnya dengan dropna() atau memberikan peringatan

    # Membersihkan kolom 'Duration' untuk menghilangkan teks dan memastikan konversi ke integer
    # Menghapus ' day' atau ' days' dari string durasi dan mengonversinya menjadi angka
    data['Duration'] = data['Duration'].replace({' days': '', ' day': ''}, regex=True).astype(int)

    # Menghapus baris dengan nilai NaN
    data = data.dropna()

    # Memastikan tidak ada data yang hilang setelah pembersihan
    print("Data Setelah Pembersihan:")
    print(data.head())

    # Simpan data yang sudah dibersihkan ke file output
    data.to_csv(output_path, index=False)
    print(f"Data telah disimpan di {output_path}")

if __name__ == "__main__":
    clean_data(
        "D:/Kampus/OnProggress/Kerja Praktek/project_analysis/data/project_tasks.csv",
        "D:/Kampus/OnProggress/Kerja Praktek/project_analysis/data/cleaned_project_tasks.csv"
    )
