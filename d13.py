import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import os
import csv
import numpy as np

files = os.listdir("stfucunt")

ez = 0
rg4 = []
cont = []
o2 = []
o3 = []
oi = []
coi = []
opinion = ["think", "maybe", "opinion", "believe"]
claim = ["is", "was", "will", "am"]
claimnot = ["think", "feel", "like", "should"]
g = 0
m = 0
#print(files)
for f in files:
    if g < 1000:
        m = 0
        with open("stfucunt/"+f) as file:
            g += 1        
            with open('stfucunt/'+str(f), 'r') as f:
                rg = f.readlines()
                #print(rg)
                for mf in range(len(rg)):
                        fard = rg[mf]
                        fard = fard.split(".")
                        #print(str(fard))
                        try:
                                for f in range(len(fard)):
                                    try:
                                        fard2 = fard[f].split("?")
                                        #print(str(fard2))
                                        for f in range(len(fard)):
                                            try:
                                                fard3 = fard2[f].split("!")
                                                for f in range(len(fard3)):
                                                    try:
                                                        fard4 = fard3[f]
                                                        #print(fard4)
                                                        #print("\n\n\n\n\n\n")
                                                        if fard4 != '':
                                                            cont.append(str(fard4))
                                                    except:
                                                        ez = 1
                                            except:
                                                ez = 1
                                    except:
                                        ez = 1
                        except:
                            ez = 1
    
for i in range(len(cont)):
    for t in range(len(opinion)):
        if opinion[t] in str(cont[i]):
            cont[i] = cont[i].replace("[", "")
            cont[i] = cont[i].replace("]", "")
            cont[i] = cont[i].replace("/", "")
            cont[i] = cont[i].replace("\n", "")
            o2.append(cont[i])
            break

    for t in range(len(claimnot)):
        if claimnot[t] not in str(cont[i]):
            for t2 in range(len(claim)):
                if claim[t2] in str(cont[i]):
                    cont[i] = cont[i].replace("[", "")
                    cont[i] = cont[i].replace("]", "")
                    cont[i] = cont[i].replace("/", "")
                    cont[i] = cont[i].replace("\n", "")
                    o3.append(cont[i])
                    break
            break


with open("text9.csv", "w") as f:
    #o3 = np.unique(o3)
    writer = csv.writer(f)
    writer.writerow(["type", "sample"]) 
    for i in range(len(o2)):
        if '"' not in o2[i]:
            writer.writerow(["Opinion/Belief", '"'+o2[i]+'"'])
        else:
            writer.writerow(["Opinion/Belief", o2[i]])

    for i2 in range(len(o3)):
        if '"' not in o3[i]:
            writer.writerow(["Claim", '"'+o3[i2]+'"'])
        else:
            writer.writerow(["Claim", (o3[i2])])

#pprint(cont)
