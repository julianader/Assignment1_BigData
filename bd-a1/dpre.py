import pandas as pd
import sys
import subprocess
from sklearn.preprocessing import OneHotEncoder

def remove_duplicates(df):
    # Removing duplicate rows
    df.drop_duplicates(inplace=True)

def fill_missing_values(df):
    # Filling missing values with specified value
    df.fillna(df.mean(), inplace=True)
    return df

def convert_sex_to_numeric(df):
    # Convert 'Sex' column to numeric
    sex_mapping = {'female': 0, 'male': 1}
    df['Sex'] = df['Sex'].map(sex_mapping)
    return df

def encode_embarked(df):
    # Feature Encoding for 'Embarked'
    encoder = OneHotEncoder()
    embarked_encoded = encoder.fit_transform(df[['Embarked']]).toarray()
    embarked_columns = ['C', 'S', 'Q', 'N']
    for i, col_name in enumerate(embarked_columns):
        df[col_name] = embarked_encoded[:, i]
    return df

def combine_features(df):
    # Combine 'SibSp' and 'Parch' to create 'Family_Size'
    df['Family_Size'] = df['SibSp'] + df['Parch']
    df.drop(['SibSp', 'Parch'], axis=1, inplace=True)
    return df

def select_relevant_features(df):
    # Select only relevant features
    correlation_matrix = df.corr()
    correlation_with_target = correlation_matrix['Survived'].abs().sort_values(ascending=False)
    relevant_features = correlation_with_target[1:6].index.tolist()
    df = df.copy()[relevant_features]  # Make a copy of the DataFrame
    return df

def discretize_age(df):
    # Discretize 'Age' into bins
    bins = [0, 12, 18, 60, df['Age'].max()]
    labels = ['Child', 'Teenager', 'Adult', 'Elderly']
    df['Age_Category'] = pd.cut(df['Age'], bins=bins, labels=labels)
    return df

def discretize_fare(df):
    # Discretize 'Fare' Feature
    num_quantiles = 5
    df['Fare_Category'] = pd.qcut(df['Fare'], q=num_quantiles, labels=False)
    return df

def data_preprocessing(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Data Cleaning
    df = remove_duplicates(df)
    df= fill_missing_values(df)
    
    # Data Transformation
    df = convert_sex_to_numeric(df)
    df = encode_embarked(df)

    # Data Reduction
    df = combine_features(df)
    df = select_relevant_features(df)

    # Data Discretization
    df = discretize_age(df)
    df = discretize_fare(df)

    # Save preprocessed data to CSV
    df.to_csv('res_dpre.csv', index=False)
    print("Preprocessed data saved successfully.")

    # Execute model script
    subprocess.run(["python3", "model.py", "res_dpre.csv"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dpre.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    data_preprocessing(file_path)
