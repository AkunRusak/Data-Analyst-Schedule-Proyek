import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data successfully loaded!")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Display summary of the data
def summarize_data(data):
    print("\nData Summary:")
    print(data.info())
    print("\nFirst 5 Rows:")
    print(data.head())

# Analyze project duration statistics
def analyze_duration(data):
    print("\nDuration Analysis:")
    print(data['Duration'].describe())

    # Plot histogram of durations
    plt.figure(figsize=(10, 6))
    plt.hist(data['Duration'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Distribution of Task Durations')
    plt.xlabel('Duration (days)')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Analyze start and finish dates
def analyze_schedule(data):
    # Convert dates to datetime format
    data['Start_Date'] = pd.to_datetime(data['Start_Date'])
    data['Finish_Date'] = pd.to_datetime(data['Finish_Date'])

    print("\nSchedule Analysis:")
    print(f"Earliest Start Date: {data['Start_Date'].min()}")
    print(f"Latest Finish Date: {data['Finish_Date'].max()}")

    # Plot Gantt chart
    plt.figure(figsize=(12, 8))
    for i, task in data.iterrows():
        plt.plot([task['Start_Date'], task['Finish_Date']], [i, i], marker='o', label=task['Task Name'] if i < 10 else "")
    plt.yticks(range(len(data)), data['Task Name'])
    plt.xlabel('Date')
    plt.ylabel('Tasks')
    plt.title('Project Gantt Chart')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize='small')
    plt.tight_layout()
    plt.show()

# Main function
def main():
    # File path (update with the actual path to your CSV file)
    file_path = 'project_schedule.csv'  # Replace with your CSV file name

    # Load the data
    data = load_data(file_path)

    if data is not None:
        summarize_data(data)
        analyze_duration(data)
        analyze_schedule(data)

if __name__ == "__main__":
    main()
