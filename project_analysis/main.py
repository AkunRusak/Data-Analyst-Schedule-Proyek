from scripts.data_cleaning import clean_data
from scripts.data_collection import collect_data
from scripts.descriptive_analysis import analyze_data
from scripts.predictive_analysis import predictive_analysis
from scripts.visualization import create_visualizations

if __name__ == "__main__":
    # Pembersihan data
    clean_data("D:/Kampus/OnProggress/Kerja Praktek/project_analysis/data/project_tasks.csv", "../data/cleaned_project_tasks.csv")
    
    # Pengumpulan data
    data = collect_data("../data/cleaned_project_tasks.csv")
    
    # Analisis deskriptif
    analyze_data("../data/cleaned_project_tasks.csv", "../outputs/descriptive_stats.json")
    
    # Analisis prediktif
    score = predictive_analysis("../data/cleaned_project_tasks.csv", "../outputs/model.pkl")
    print(f"Model R^2 Score: {score}")
    
    # Visualisasi
    create_visualizations("../data/cleaned_project_tasks.csv", "../outputs/visualizations")
    print("Proses selesai.")
