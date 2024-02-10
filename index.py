import nltk
import spacy

nltk.download('punkt')
# Carregando o modelo spaCy
nlp = spacy.load('en_core_web_sm')

from nltk.tokenize import word_tokenize

text = "Hello, world! Welcome to the world of Natural Language Processing."
tokens = word_tokenize(text)
print(tokens)

doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for ent in doc.ents:
    print(ent.text, ent.label_)

from textblob import TextBlob

feedback = TextBlob("I love this product, it's absolutely amazing!")
print(feedback.sentiment)