def collect_data(cleaned_data):
    # Filter data untuk keperluan analisis tertentu
    collected_data = cleaned_data[['Task Name', 'Duration', 'Start_Date', 'Finish_Date']]
    return collected_data
