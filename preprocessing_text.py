from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import contractions
import re
import string
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

# Tokenization and Stopwords Removal
stop_words = set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()


# preprocess text
def preprocess_and_clean_text(text):
    text = str(text)

    text = contractions.fix(text)  # Expand contractions (e.g., "don't" -> "do not")

    # Preprocessing
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'\[.*?\]', '', text)  # Remove text in square brackets
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Remove links
    text = re.sub(r'<.*?>+', '', text)  # Remove HTML tags
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)  # Remove punctuation
    text = re.sub(r'\n', '', text)  # Remove newlines
    text = re.sub(r'\w*\d\w*', '', text)  # Remove words containing numbers
    text = text.strip()  # Remove extra whitespace
    text = text.lower()  # Lowercase text
    text = re.sub(r'[^\x00-\x7f]', r'', text)  # Remove non-ASCII characters

    print(text)
    return text


# Tokenization, Stopwords Removal, and Lemmatization
def remove_stopwords_and_lemmatize(text):
    text = word_tokenize(text)
    text = [lemmatizer.lemmatize(word) for word in text if word not in stop_words]
    return ' '.join(text)


# Preprocess and clean text
def preprocess_text(text):
    text = preprocess_and_clean_text(text)
    text = remove_stopwords_and_lemmatize(text)
    return text


# Test the function
tx = "don't, like"
print(preprocess_text(tx))
# output: 'like'