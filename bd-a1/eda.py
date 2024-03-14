import pandas as pd
import sys

def exploratory_data_analysis(file_path):
    df = pd.read_csv(file_path)

    insights = [
        "1. The average age of passengers is {} years.".format(df['Age'].mean()),
        "2. The maximum fare paid by a passenger is ${}.".format(df['Fare'].max()),
        "3. There are {} unique passenger classes in the dataset.".format(df['Pclass'].nunique())
    ]

    for i, insight in enumerate(insights):
        with open(f'eda-in-{i+1}.txt', 'w') as f:
            f.write(insight)

    print("Exploratory data analysis insights saved successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python eda.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    exploratory_data_analysis(file_path)
