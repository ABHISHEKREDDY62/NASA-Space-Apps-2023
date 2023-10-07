from sentence_transformers import SentenceTransformer, util
import pandas as pd
sentences = "Airplane safety"

data=pd.read_csv("final_training_data.csv")

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

#Compute embedding for both lists
l=[]
data["Summary"]=[str(i) for i in data["Summary"].values]
for i in data["Summary"].values:
    embedding_1= model.encode(sentences, convert_to_tensor=True)
    embedding_2 = model.encode(i, convert_to_tensor=True)
    l.append(util.pytorch_cos_sim(embedding_1, embedding_2))
data["similarity"]=l
data=data.sort_values(by="similarity",ascending=False)
print(data["Summary"].values[0])