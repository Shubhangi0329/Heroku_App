# -*- coding: utf-8 -*-
"""salary_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HW4gp_8dQhyc_L4PY3tDIQPomuItEfqK
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

dataset=pd.read_csv('Salary_data.csv')

dataset

dataset['experience'].fillna(0,inplace=True)

dataset['test_score'].fillna(dataset['test_score'].mean(),inplace=True)

dataset

def convert_to_int(word):
    word_dict={0:0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,
              'twelve':12,'zero':0}
    return word_dict[word]

dataset['experience']=dataset['experience'].apply(lambda x: convert_to_int(x))

X=dataset.iloc[:,1:4]

Y=dataset.iloc[:,-1]

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(X,Y)

pickle.dump(regressor,open('model.pkl','wb'))

model=pickle.load(open('model.pkl','rb'))

print(model.predict([[2,9,6]]))