import spacy
# from nltk.corpus import gutenberg  as the_corpus

nlp= spacy.load("en_core_web_sm")
with open("./data/wiki_us.txt", "r") as data_file:
    text= data_file.read()
doc= nlp(text)
# print(f"Doc Length: {len(doc)} \n{doc}")

# doc tokens words
# for token in doc[:10]:
#     print(token)

# doc sentence segmentations
sentence1= list(doc.sents)[0]
# print(sentence1)

# Token Attributes
token1= sentence1[15]
print(f"text: {token1.text}")
# print(f"head: {token1.head}")
# print(f"left_edge: {token1.left_edge}")
# print(f"right_edge: {token1.right_edge}")
print(f"ent_type_: {token1.ent_type_}")
# print(f"ent_iob_: {token1.ent_iob_}")
# print(f"lemma_: {token1.lemma_}")
# print(f"morph: {token1.morph}")
# print(f"pos_: {token1.pos_}")
# print(f"dep_: {token1.dep_}")
# print(f"lang_: {token1.lang_}")


