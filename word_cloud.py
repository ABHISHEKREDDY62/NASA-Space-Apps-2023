import pickle
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from keybert import KeyBERT
import re
import numpy as np
from keyphrase_vectorizers import KeyphraseCountVectorizer
from summary import *
import re,nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
import contractions
docs=[]
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("punkt")
nltk.download("stopwords")
stops=set(stopwords.words("english"))
words=[]
def weightage(word,text,number_of_documents=1):
    # print(word)
    word_list = re.findall(word,text)
    number_of_times_word_appeared =len(word_list)
    tf = number_of_times_word_appeared/float(len(text))
    idf = np.log((number_of_documents)/float(number_of_times_word_appeared))
    tf_idf = tf*idf
    return number_of_times_word_appeared,tf,idf ,tf_idf   
 
def clean_content(sentence):
    sentence=re.sub(r'\<[^<>]*\>','',sentence)
    sentence=re.sub(r'^\W+|\W+$',' ',sentence)
    sentence=re.sub(r'\s',' ',sentence)
    sentence=re.sub(r'[^a-zA-Z0-9]',' ',sentence)
    sentence =re.sub(r'/\r?\n|\r/g',' ',sentence)
    sentence = re.sub(r's/\([^)]*\)///g',' ',sentence)
    sentence = word_tokenize(sentence)
    sentence = [i for i in sentence if i not in stops]
    return sentence

def process_sentences(word):
    
    word=''.join([i for i in word if not i.isdigit()])
    l = nltk.stem.WordNetLemmatizer()    
        
            
    if word not in string.punctuation and word.lower() not in stops:
            
            
        stem=l.lemmatize(word)
        word=str(stem)
    return word

def keywords(pdf_data,id):
    text=pdf_data.split(" ")
    



    new_text={}
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    for i in text:
        
        
        if len(i)<=3:
            continue
        i=clean_content(i)
        i=process_sentences(i)
        new_text[i.lower()]=new_text.get(i.lower(),0)+1

    new_text=list(new_text.keys())
    for i in new_text:
        number_of_times_word_appeared,tf,idf ,tf_idf=weightage(i,' '.join(new_text))
        l1.append(number_of_times_word_appeared)
        l2.append(tf)
        l3.append(idf)
        l4.append(tf_idf)
    df=pd.DataFrame(data={"keywords":new_text})
    df['number_of_times_word_appeared'] = l1
    df['tf'] = l2
    df['idf'] = l3
    df['tf_idf'] = l4
    
    df = df.sort_values('tf_idf',ascending=False)
    df.drop_duplicates(subset="keywords")
    df.to_csv("tfidf.csv")
    text=' '.join(df["keywords"].values)
    print(text)
    word_cloud = WordCloud(background_color="black",max_words=300,\
                max_font_size=30,min_font_size=0.00000001,\
                random_state=42).generate(text)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(f'C:\\Users\\sudha\\Downloads\\NASA Space Apps 2023\\wordclouds\\{id}.jpg')
    return text

   
