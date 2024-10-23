from gensim.summarization import summarize
 # 0


def generate_summary(text, ratio=0.2):
 # def generate_summary(text, ratio=0.2):
    """Generate a summary of the text using Gensim's summarize function."""

    try:

        summary = summarize(text, ratio=ratio)

        return summary

    except ValueError:

        return "Text is too short to summarize."



def summarize_sentences(sentences, ratio=0.2):

    """Summarize a list of sentences."""

    text = ' '.join(sentences)

    return generate_summary(text, ratio)



