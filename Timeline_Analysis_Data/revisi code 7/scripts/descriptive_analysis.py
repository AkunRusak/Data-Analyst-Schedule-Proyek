def descriptive_analysis(data):
    print("Statistik Durasi (hari):")
    print(data['Duration'].describe())
    
    print("\nRentang Tanggal:")
    print(f"Mulai dari {data['Start_Date'].min()} sampai {data['Finish_Date'].max()}")
    
    print("\nJumlah Task Berdasarkan Durasi:")
    print(data['Duration'].value_counts())
