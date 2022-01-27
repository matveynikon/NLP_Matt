import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import os
import csv
import pandas
df = pandas.read_csv('text.csv')

print(df["text"])
for f in df["text"]:
    with open(f) as file:
        for line in file:
            print(str(line))
