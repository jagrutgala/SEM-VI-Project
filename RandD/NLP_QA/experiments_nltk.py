from cgitb import text
import nltk
from nltk import WordNetLemmatizer
from nltk.book import text3
from string import punctuation

print(text3[:25])
print(f"Tokens in text3 {len(text3)}")

distinct_text= sorted(set(text3))
print(distinct_text[-20:])
print(f"Distinct Tokens in text3 {len(set(text3))}")

distinct_text_no_punctuation= [i for i in list(distinct_text) if i not in punctuation]
print(f"Distinct Tokens (No Punctuations) {distinct_text_no_punctuation[:25]}")
lemmatizer= WordNetLemmatizer()
distinct_text_lemmatized= set([lemmatizer.lemmatize(i) for i in distinct_text_no_punctuation])
print(f"Distinct Lemmatizied Tokens (No Punctuations) {list(distinct_text_lemmatized)[:25]}")
print(f"Length of Distinct Lemmatizied Tokens {len(distinct_text_lemmatized)}")

# print(list(text3))





class Document:
    def __init__(self, text) -> None:
        self.text= text
    
    # Document Pipeline
    # text -> tokenize(words) -> tag -> parse -> ner    ] -> Document
    #                         -> lemmatize              ] ^
    #      -> tokenize(sents)                           ] ^
    #                                                   ] ^
