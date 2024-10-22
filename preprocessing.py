import nltk

# Download NLTK resources
nltk.download('punkt')

def preprocess_text(text):
    """Preprocess the text by tokenizing sentences."""
    sentences = nltk.sent_tokenize(text)
    return sentences
 # 8
