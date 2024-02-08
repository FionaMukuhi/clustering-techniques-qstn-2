import json
from sklearn.cluster import KMeans
from generate_vectors import generate_tfidf_vectors
from load_data import load_preprocessed_data_with_urls

def apply_kmeans(tfidf_matrix, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(tfidf_matrix)
    return kmeans.labels_

if __name__ == "__main__":
    file_path = './preprocessed_articles_with_urls.json'
    articles, urls = load_preprocessed_data_with_urls(file_path)  
    tfidf_matrix, tfidf_vectorizer = generate_tfidf_vectors(articles)
    cluster_labels = apply_kmeans(tfidf_matrix)

    # Organize articles by their assigned cluster label, including URLs
    clustered_articles = {}
    for label, (article, url) in zip(cluster_labels, zip(articles, urls)):
        label_str = str(label)  # Convert label to string
        clustered_articles.setdefault(label_str, []).append({"article": article, "url": url})

    # Save the clustered articles with URLs to a JSON file
    with open('clustered_articles_with_urls.json', 'w') as f:
        json.dump(clustered_articles, f, indent=4)

    print(f"Applied K-Means clustering. First 10 cluster assignments: {cluster_labels[:10]}")
