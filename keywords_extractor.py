from keybert import KeyBERT
from keyphrase_vectorizers import KeyphraseCountVectorizer
def keywords(file):
    with open(file,"r") as f:
        docs=list(f.read())
    kw_model=KeyBERT()
    keywords=kw_model.extract_keywords(docs=docs, vectorizer=KeyphraseCountVectorizer())
    print(keywords)
    # vectorizer = KeyphraseCountVectorizer()
    # document_keyphrase_matrix = vectorizer.fit_transform(docs).toarray()
    # keyphrases = vectorizer.get_feature_names_out()
    # print(keyphrases)
keywords("19710021280_clean.txt")
