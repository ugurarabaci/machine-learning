# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:30:42 2020

@author: Samsung
"""


#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.veri onisleme
#2.1.veri yukleme
veriler = pd.read_csv("veriler.csv")
#test
print(veriler)


x=veriler.iloc[:,1:4].values#bağımsız değişken
y=veriler.iloc[:,4:].values#bağımlı değişken



#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)

#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)


from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

knn = KNeighborsClassifier(n_neighbors=1, metric='minkowski')
knn.fit(X_train, y_train)

y_pred = knn.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)