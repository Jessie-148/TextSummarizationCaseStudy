import nltk



# Download NLTK resources

nltk.download('punkt')



def preprocess_text(text):

    """Preprocess the text by tokenizing sentences."""

    sentences = nltk.sent_tokenize(text)

    return sentences



def clean_text(text):

    """Clean the text by removing unnecessary characters."""

    # You can add more cleaning steps as needed

    return text.strip()



