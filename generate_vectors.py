from sklearn.feature_extraction.text import TfidfVectorizer
# Make sure to import the updated loading function
from load_data import load_preprocessed_data_with_urls

def generate_tfidf_vectors(articles):
    tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(articles)
    return tfidf_matrix, tfidf_vectorizer

if __name__ == "__main__":
    file_path = './preprocessed_articles_with_urls.json'
    articles, urls = load_preprocessed_data_with_urls(file_path)  
    tfidf_matrix, tfidf_vectorizer = generate_tfidf_vectors(articles)
    print(f"Generated TF-IDF matrix with shape {tfidf_matrix.shape}.")
