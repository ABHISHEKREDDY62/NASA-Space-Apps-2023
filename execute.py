from flask import Flask, render_template, session, request, redirect, url_for,flash
from sentence_transformers import SentenceTransformer, util
import pandas as pd
import string   

#from search import *
#from get_pdf_details import *
#from word_cloud import *
#from Seq2Ser import *

app = Flask(__name__,template_folder='templates')
@app.route("/")
def search_index():
    return render_template("index.html")
    
@app.route("/search_pdf", methods=["POST", "GET"])
def search():
    q = request.form["search"]
    print(q)
    l=[]
    data=pd.read_csv("senetence_similarity.csv")
    # model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    # data["Summary"]=[str(i) for i in data["Summary"].values]
    # for i in data["Summary"].values:
    #     embedding_1= model.encode(q, convert_to_tensor=True)
    #     embedding_2 = model.encode(i, convert_to_tensor=True)
    #     l.append(util.pytorch_cos_sim(embedding_1, embedding_2))
    # data["similarity"]=l
    # data=data.sort_values(by="similarity",ascending=False)
    # data.to_csv("senetence_similarity.csv")
    document_id=data["Document ID"].values[:10]
    print(data["similarity"].values)
    # results = search_on_keyword(q)
    # print(results)
    # pdf_details = fetch_pdf_details(results)
    # print(pdf_details["ids"])

    # if request.method == 'POST':
    #     return render_template("embed.html", query=q, results=pdf_details["title"], 
    #     cats = pdf_details["cats"], ids = pdf_details["ids"])
    return render_template("embed_after.html",query=q,document_id=document_id)

@app.route("/pdf_details/<pdf_id>", methods=["POST", "GET"])
def after_search(pdf_id):
    data=pd.read_csv("final_training_data.csv")
    description=data[data["Document ID"]==int(pdf_id)]["Description"].values[0]
    description=description.split(",")
    new=[]
    for i in range(len(description)):
        description[i] = description[i].translate(str.maketrans('', '', string.punctuation))
        if i==1:
            new.append("Document Type: "+description[i])
        elif i==2:
            new.append("Date Acquired: "+description[i])
        elif i==3:
            new.append("Publication Date: "+description[i])
        elif i==4:
            new.append("Publication Information: "+description[i])
        else:
            new.append(description[i])
        
            
    summary=data[data["Document ID"]==int(pdf_id)]["Summary"].values[0]
    print("this summary",summary)
    print(data.columns)
    #generate_wordcloud(pdf_id)
    #cleaned_data(pdf_id)
    return render_template("after_search.html", details = new[:-2],ID=pdf_id,summary=summary)

@app.route("/embed")
def embed():
    return render_template("embed.html")

if __name__=="__main__":
    app.debug=True
    app.run(host="127.0.0.1",port=5000)