import spacy

# ładujemy model języka polskiego
nlp = spacy.load("pl_core_news_sm")

def analyze_text(text: str):
    doc = nlp(text)
    return [
        {"token": token.text, "pos": token.pos_, "dep": token.dep_}
        for token in doc
    ]
