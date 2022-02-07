import spacy
nlp= spacy.load("en_core_web_sm")
print(f"spacy pipeline {nlp.pipe_names}")
print(f"spacy pipeline components {nlp.component_names}")
print(f"spacy pipeline disabled {nlp.disabled}")


inputfile_name= "input_data.txt"
raw_text= open(f"./data/{inputfile_name}", "r").read()
doc= nlp(raw_text)

# print(f"entities: {doc.ents}")
print("\n")
for token in doc:
    print(f"text: {token.text}")
    print(f"pos: {token.pos_}")
    print(f"tag: {token.tag_}")
    print(f"lemma: {token.lemma_}")
    print(f"dependency: {token.dep_}")
    print(f"entity: {token.ent_type_}")
    print()


# print()
# for sen in doc.sents:

# Done!

# Apple is looking at buying U.K. startup for $1 billion.