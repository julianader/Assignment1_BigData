import pandas as pd
import sys
import subprocess

def data_preprocessing(file_path):
    df = pd.read_csv(file_path)

    # Example preprocessing steps
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    df.to_csv('res_dpre.csv', index=False)
    print("Preprocessed data saved successfully.")

    subprocess.run(["python", "eda.py", "res_dpre.csv"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dpre.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    data_preprocessing(file_path)
