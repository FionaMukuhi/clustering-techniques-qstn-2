import json

def load_preprocessed_data_with_urls(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    articles = [article['preprocessed_text'] for article in data]
    urls = [article['url'] for article in data]
    return articles, urls

if __name__ == "__main__":
    file_path = './preprocessed_articles_with_urls.json'
    articles = load_preprocessed_data_with_urls(file_path)
    print(f"Loaded {len(articles)} articles.")
