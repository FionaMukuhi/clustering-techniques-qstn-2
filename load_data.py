import json

# def load_preprocessed_data(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     print(type(data)) 
#     if data:  # Ensures data is not empty
#         print(data[0])
#         print(type(data[0]))  # This should show <class 'dict'>

#     articles = [article['preprocessed_text'] for article in data]
#     return articles

def load_preprocessed_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    file_path = './preprocessed_articles.json'
    articles = load_preprocessed_data(file_path)
    print(f"Loaded {len(articles)} articles.")
