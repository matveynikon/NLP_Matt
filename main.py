import numpy as np
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import os
files = os.listdir("t")

sents = []
labels = []
big = []
c = 0
print(files)
for f in files:
    try:
        with open(f) as file:
            if c > 10:
                break
            c + 1
            for line in file:
                l = line.split(". ")
                if(l != ['\n']):
                    sents.append(l)
    except:
        print("JLKJ")

for i in range(len(sents)):
    s1 = sents[i]
    for j in range(len(s1)):
        print(s1[j])
        big.append(s1[j])
        if("believe" in s1[j]):
            labels.append("Claim")
        elif("despite" in s1[j]):
            labels.append("Counter argument")
        else:
            labels.append("?")

x = big
y = labels
cv = CountVectorizer()
x = cv.fit_transform(x)
model = MultinomialNB()
model.fit(x, y)

news_headline = "believe jeff"
data = cv.transform([news_headline]).toarray()
print(news_headline)
print(model.predict(data))
