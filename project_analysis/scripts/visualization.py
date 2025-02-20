import pandas as pd
import matplotlib.pyplot as plt

def create_visualizations(file_path, output_path):
    data = pd.read_csv(file_path)
    
    # Visualisasi Durasi per Bagian
    plt.figure(figsize=(10, 6))
    sections = data[data['Task Name'].str.contains('SECTION', case=False)]
    plt.bar(sections['Task Name'], sections['Duration'], color='skyblue')
    plt.title('Durasi per Bagian')
    plt.xlabel('Bagian')
    plt.ylabel('Durasi (hari)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_path}/duration_per_section.png")

if __name__ == "__main__":
    create_visualizations("../data/cleaned_project_tasks.csv", "../outputs/visualizations")
