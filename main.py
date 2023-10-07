from gpt2 import *
from word_cloud import *
from summary import *
from data import *
import pandas as pd
k=1425
if __name__=="__main__":
    df=pd.read_csv("final_training_data1.csv")
    l=[]
    l.append(df)
    for i in range(1000):
        
        data=collect_pdf(k)
            
        
        for i,j in data.items():
            try:
                print("Reading Document",i)
                pdf_data,text=read(i)
            

                
                #print(pdf_data)
                print("Completed Reading Document",i)
                summary=pdf_summary(pdf_data)
                print("Completed Summary of the Document",i)
                keyword=keywords(pdf_data,i)
                df=pd.DataFrame(data={'Document ID':[i],"Description":[j],"Summary":[summary],"keywords":[keyword],"pdf_data":[text]})
                l.append(df)
                df=pd.concat(l)
                df.head()
                df.to_csv("final_training_data1.csv")
            except:
                print("in except")
                continue   
         
        k+=25

        




