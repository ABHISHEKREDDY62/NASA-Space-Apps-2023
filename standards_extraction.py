import pickle
import re
with open("output.pickle","rb") as f:
    data1=pickle.load(f)
    m=0
    standards={}
    pattern = r'\d\.'
    print("while",bool(re.match(pattern, "7 of 47")))
    for keys,values in data1.items():
            #if (m>=25 and m<=26) or (m>=29 and m<=40) or (m>=42 and m<=45):
        # if m==34:
        #     for k in values:
        #         print("Keys: ",keys,"Value: ",k)
        #         k = re.sub(r'[0-9]', '', str(k))
        #         print("Keys: ",keys,"Value: ",k)
        #         result = ''.join([i for i in k if not i.isdigit()])
        # m+=1
        try:
            matches = re.findall(pattern, str(keys[0:6]))
            if matches:
                print(keys)
                standards.update({keys:values})
        except:
            continue
    print(standards)
    with open("standards1.pickle","wb") as f:
        pickle.dump(standards,f)
