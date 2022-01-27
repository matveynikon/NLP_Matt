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
question = ["?"]
g = 0
m = 0
#print(files)
for f in files:
    if g < 10:
        m = 0
        with open("stfucunt/"+f) as file:
            g += 1        
            with open('stfucunt/'+str(f), 'r') as f:
                rg = f.readlines()
                #print(rg)
                for mf in range(len(rg)):
                        fard = rg[mf]
                        fard = fard.split(".")
                        print(str(fard))
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
                                                        print(fard4)
                                                        print("\n\n\n\n\n\n")
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
            cont[i] = cont[i].replace("'", "")
            cont[i] = cont[i].replace("/", "")
            #cont[i] = cont[i].replace('"', '')
            cont[i] = cont[i].replace("\n", "")
            o2.append(cont[i])
            break

cont2 = []
oi = []
coi = []
g = 0
rg4 = []

for f in files:
    if g < 10:
        m = 0
        with open("stfucunt/"+f) as file:
            g += 1        
            with open('stfucunt/'+str(f), 'r') as f:
                rg = f.readlines()
                #print(rg)
                for mf in range(len(rg)):
                        fard = rg[mf]
                        fard = fard.split(".")
                        print(str(fard))
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
                                                        print(fard4)
                                                        print("\n\n\n\n\n\n")
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
    
for i in range(len(cont2)):
    for t in range(len(question)):
        if question[t] in str(cont2[i]):
            cont2[i] = cont2[i].replace("[", "")
            cont2[i] = cont2[i].replace("]", "")
            cont2[i] = cont2[i].replace("'", "")
            cont2[i] = cont2[i].replace("/", "")
            #cont2[i] = cont2[i].replace('"', '')
            cont2[i] = cont2[i].replace("\n", "")
            o3.append(cont2[i])
            break

with open("text.csv", "w") as f:
    o3 = np.unique(o3)
    writer = csv.writer(f)
    writer.writerow(["type", "sample"]) 
    for i in range(len(o2)):
        writer.writerow(["Opinion/Belief", o2[i]])
    for i in range(len(o3)):
        writer.writerow(["Question", o3[i]])

#pprint(cont)
