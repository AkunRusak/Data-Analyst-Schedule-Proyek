if __name__ == "__main__":
    file_path = "path_to_your_csv_file.csv"  # Ganti dengan lokasi file Anda
    
    # Data Cleaning
    data_cleaning = data_cleaning(file_path)
    print("Data setelah dibersihkan:")
    print(data_cleaning.head())
    
    # Data Collection
    data_collection = collect_data(cleaned_data)
    
    # Descriptive Analysis
    print("\nAnalisis Deskriptif:")
    descriptive_analysis(data_collection)
    
    # Predictive Analysis
    print("\nAnalisis Prediktif:")
    predictive_analysis(data_collection)
    
    # Visualization
    print("\nVisualisasi Data:")
    visualize_data(data_collection)
