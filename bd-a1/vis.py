import matplotlib.pyplot as plt
import pandas as pd

# Create a simple visualization
def create_visualization(file_path):
    plt.scatter(data['Cabin'], data['Survived'])
    plt.xlabel('Cabin')
    plt.ylabel('Survived')
    plt.title('Simple Visualization')
    plt.savefig('vis.png')
    plt.close()

if __name__ == "__main__":
    # Load your data
    data = pd.read_csv('file_path')

    # Create visualization
    create_visualization(data)
