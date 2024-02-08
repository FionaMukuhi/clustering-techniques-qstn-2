import json
from sklearn.cluster import KMeans
from generate_vectors import generate_tfidf_vectors, load_preprocessed_data

def apply_kmeans(tfidf_matrix, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(tfidf_matrix)
    return kmeans.labels_

if __name__ == "__main__":
    file_path = './preprocessed_articles.json'
    articles = load_preprocessed_data(file_path)
    tfidf_matrix, feature_names = generate_tfidf_vectors(articles)
    cluster_labels = apply_kmeans(tfidf_matrix)

    # Organize articles by their assigned cluster label, converting labels to strings
    clustered_articles = {}
    for label, article in zip(cluster_labels, articles):
        label_str = str(label)  # Convert label to string
        clustered_articles.setdefault(label_str, []).append(article)

    # Save the clustered articles to a JSON file
    with open('clustered_articles.json', 'w') as f:
        json.dump(clustered_articles, f, indent=4)

    print(f"Applied K-Means clustering. First 10 cluster assignments: {cluster_labels[:10]}")
