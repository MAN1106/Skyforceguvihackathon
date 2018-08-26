import pandas as pd
from gensim.models import Word2Vec
df=pd.read_csv("train.csv")

b=Word2Vec(df)
print(b.most_similiar('Your',topn=5))
