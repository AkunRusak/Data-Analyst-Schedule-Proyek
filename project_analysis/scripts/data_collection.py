import pandas as pd

def collect_data(file_path):
    return pd.read_csv(file_path)

if __name__ == "__main__":
    data = collect_data("../data/cleaned_project_tasks.csv")
    print(data.head())  # Menampilkan 5 baris pertama untuk memverifikasi data
