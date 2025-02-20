import matplotlib.pyplot as plt

def visualize_data(data):
    plt.figure(figsize=(10, 6))
    
    # Histogram Durasi
    plt.hist(data['Duration'], bins=15, color='skyblue', edgecolor='black')
    plt.title('Distribusi Durasi Task')
    plt.xlabel('Durasi (hari)')
    plt.ylabel('Frekuensi')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()
