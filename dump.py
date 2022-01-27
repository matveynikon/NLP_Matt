import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("text.csv")

x = np.array(data["sample"])
y = np.array(data["type"])

cv = CountVectorizer()
x = cv.fit_transform(x)

model = MultinomialNB()
model.fit(x, y)

news_headline = "why are you gae?"
data = cv.transform([news_headline]).toarray()
print(news_headline)
print(model.predict(data))