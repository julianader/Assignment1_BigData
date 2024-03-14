import matplotlib.pyplot as plt
import pandas as pd

# Create a simple visualization
def create_visualization(data):
    plt.scatter(data['Feature1'], data['Feature2'])
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Simple Visualization')
    plt.savefig('vis.png')
    plt.close()

if __name__ == "__main__":
    # Load your data
    data = pd.read_csv('your_data.csv')

    # Create visualization
    create_visualization(data)
