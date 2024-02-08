import json
import spacy
import string
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# NLTK Stop words
stop_words = set(stopwords.words('english'))

# Function to clean and lemmatize the text
def preprocess_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize and lemmatize
    doc = nlp(text)
    lemmatized = [token.lemma_ for token in doc if token.lemma_ not in stop_words]
    
    # Remove stop words and non-alphabetic tokens
    cleaned_text = ' '.join([word for word in lemmatized if word.isalpha()])
    
    return cleaned_text

# Load the articles
with open('articles.json', 'r') as f:
    articles = json.load(f)

# Preprocess the articles
preprocessed_articles = [preprocess_text(article['content'] if 'content' in article else '') for article in articles]

# Save the preprocessed articles to a new JSON file
with open('preprocessed_articles.json', 'w') as f:
    json.dump(preprocessed_articles, f, ensure_ascii=False, indent=4)

print('Preprocessed and saved articles successfully!')
