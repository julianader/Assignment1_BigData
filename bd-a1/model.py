import pandas as pd
from sklearn.cluster import KMeans

def k_means_algorithm(file_path):
    # Select columns suitable for K-means
    X = data[['Feature1', 'Feature2']]  # Adjust column names as per your data

    # Initialize K-means model
    kmeans = KMeans(n_clusters=3)

    # Fit the model
    kmeans.fit(X)

    # Get the number of records in each cluster
    cluster_counts = pd.Series(kmeans.labels_).value_counts().sort_index()

    # Save the number of records in each cluster
    with open('k.txt', 'w') as f:
        f.write(cluster_counts.to_string())

if __name__ == "__main__":
    # Load your data
    data = pd.read_csv('file_path')

    # Implement K-means algorithm
    k_means_algorithm(data)
