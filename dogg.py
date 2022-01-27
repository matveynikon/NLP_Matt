import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import os
import csv
import numpy as np

files = os.listdir("stfucunt")

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
        m = 0
        with open("stfucunt/"+f) as file:
            g += 1        
            with open('stfucunt/'+str(f), 'r') as f:
                rg = f.readlines()
                #print(rg)
                for mf in range(len(rg)):
                    rg3 = rg[mf]
                    rg3.split(".")
                    for j in range(len(rg3)):
                        try:
                            rg3[j].split("?")
                        except:
                            print("k")
                    for j in range(len(rg3)):
                        try:
                            rg3[j].split("!")
                        except:
                            print("k")
                    for j in range(len(rg3)):
                        try:
                            rg3[j].split("...")
                        except:
                            print("k")
                    cont.append(str(rg3))
    
for i in range(len(cont)):
    for t in range(len(opinion)):
        if opinion[t] in str(cont[i]):
            o2.append(cont[i])
            break

cont2 = []
oi = []
coi = []
g = 0

for f in files:
        m = 0
        with open("stfucunt/"+f) as file:
            g += 1        
            with open('stfucunt/'+str(f), 'r') as f:
                #print(f.readlines())
                rg = f.readlines()
                for mf in range(len(rg)-1):
                    rg3 = rg[mf]
                    for j in range(len(rg3)-1):
                        try:
                            rg3[j].split("?")
                        except:
                            print("k")
                    for j in range(len(rg3)-1):
                        try:
                            rg3[j].split("!")
                        except:
                            print("k")
                    for j in range(len(rg3)-1):
                        try:
                            rg3[j].split("...")
                        except:
                            print("k")
                    #print(rg3)
                    cont2.append(str(rg3))
    
for i in range(len(cont2)):
    for t in range(len(question)):
        if question[t] in str(cont2[i]):
            o3.append(cont2[i])
            break

with open("text.csv", "w") as f:
    o3 = np.unique(o3)
    writer = csv.writer(f)
    writer.writerow(["type", "sample"]) 
    for i in range(len(o3)):
        writer.writerow(["Question", o3[i]])
    for i in range(len(o2)):
        writer.writerow(["Opinion/Belief", o2[i]])

#pprint(cont)