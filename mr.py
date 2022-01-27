import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import os
import csv

files = os.listdir("stfucunt")

cont = []
o2 = []
oi = []
opinion = ["think", "maybe", "probably", "opinion"]
g = 0
m = 0
print(files)
for f in files:
    try:
        m = 0
        with open("stfucunt/"+f) as file:
            g += 1   
            for line in file:      
                with open('stfucunt/'+str(f), 'r') as f:
                    #print(f.readlines())
                    cont.append(f.readlines())
    except:
        print("gangsta rap made me do it")
    
print(cont)

for i in range(len(cont)):
    for t in range(len(opinion)):
        if opinion[t] in str(cont[i]):
            o2.append(cont[i])
            
print("\n\n\n\n\n\n\n\n\n")
print(o2)
for n in range(len(o2)):
    oi.append(cont.index(o2[n]))

print("\n\n\n\n\n\n\n\n\n")
print(oi)
