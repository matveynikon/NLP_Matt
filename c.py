import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import os
import csv

files = os.listdir("t")

sents = []
labels = []
big = []
cont = []
claim = ["is why", "i think", "evidence", "because", "should"]
coclaim = ["but", "instead", "shouldn't", "isn't", "no"]
belief = ["believe", "why", "should", "shouldn't", "argue"]
claims = []
c = 0
cc = 0
b = 0
g = 0
v = 0
print(files)
for f in files:
    with open("t/"+f) as file:
        for line in file:
            if line != '\n':
                v += 1
                #print(cont)
                #print(line)   
                l = line.split("\n")
                #print(l)
                for j in range(len(l)):
                    try:
                        l.remove('\n')
                    except:
                        print("er")
                    with open('stfucunt/'+str(v)+str(j), 'w') as f:
                        f.write(str(l))
                        ef = 'stfucunt/'+str(v)+str(j)
                        cont.append(ef)
"""
with open("text.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["text"]) 
    for i in range(len(cont)):
        writer.writerow([cont[i]])
"""
print(cont)
