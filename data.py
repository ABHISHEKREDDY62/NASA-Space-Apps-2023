#File is to import data from NTRS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import pickle
url='https://ntrs.nasa.gov/search?q=safety&page=%7B%22size%22:25,%22from%22:0%7D'


#l=["Document ID","Document Type","External Source(s)","Authors","Date Acquired","Publication Date","Publication Information","Subject Category","Report/Patent Number","Meeting Information","Accession Number","Funding Number(s)","Distribution Limits","Copyright","Technical Review","Keywords"]
def collect_pdf(k):
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : 'C:\\Users\\sudha\\Downloads\\NASA Space Apps Challenge\\pdf'}
    chromeOptions.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(options=chromeOptions)

    
    final_df=[]
    data={}
    # with open("output.pickle","rb") as f:
    #     data=pickle.load(f)
    # print(data)
    
    url=f'https://ntrs.nasa.gov/search?q=safety&page=%7B%22size%22:25,%22from%22:{k}%7D'
    driver.get(url)
    time.sleep(3)
    
    val=driver.find_elements("xpath",'//div[@class="data"]')
    label=driver.find_elements("xpath",'//div[@class="label"]')
    chip=driver.find_elements("xpath",'//mat-chip[@class="mat-chip mat-focus-indicator mat-primary mat-standard-chip ng-star-inserted"]')
    
    for i in val:
        try:
            if int(i.text) and len(i.text)==11:
                doc_id=i.text
                print(doc_id)
                continue
        except:
            if data.get(doc_id)!=None:
                data[doc_id].append(i.text)
            else:
                data.update({doc_id:[i.text]})
    

    
    print(data)
    with open("page.txt",'a') as f:
        f.write(str(k)+"\n")
    for btn in driver.find_elements("xpath",f'//a[@title="Download Document"]'):
        btn.click()
        time.sleep(20)
        

    
        
    time.sleep(3)
    driver.close()
    return data

