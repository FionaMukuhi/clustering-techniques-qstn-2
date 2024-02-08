from sklearn.feature_extraction.text import TfidfVectorizer
from load_data import load_preprocessed_data

def generate_tfidf_vectors(articles):
    tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(articles)
    return tfidf_matrix, tfidf_vectorizer

if __name__ == "__main__":
    file_path = './preprocessed_articles.json'
    articles = load_preprocessed_data(file_path)
    tfidf_matrix, tfidf_vectorizer = generate_tfidf_vectors(articles)
    print(f"Generated TF-IDF matrix with shape {tfidf_matrix.shape}.")
