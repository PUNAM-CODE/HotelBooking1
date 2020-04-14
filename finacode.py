# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np

data=pd.read_csv("F:/data science r studio/proj practice/hote booking/hotel_bookings.csv")

data.head(10)

data.shape

data.isnull().sum()

data.drop(inplace=True, axis=1, labels=['agent', 'company','hotel','reservation_status_date'])

cols = data.columns
for i in cols:
    print('\n',i,'\n',data[i].unique(),'\n','-'*80)

data.isnull().sum()

data.fillna(data.mode().iloc[0], inplace=True)

data.head()

X = data.iloc[:,1:]
y = data.iloc[:,0]

# Importing relevant libraries
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer

#Implementing Column Transformer
ct = make_column_transformer(
    (OneHotEncoder(),['meal','distribution_channel','reservation_status','country','arrival_date_month','market_segment','deposit_type','customer_type', 'reserved_room_type','assigned_room_type' ]), remainder = 'passthrough'
    )

X = ct.fit_transform(X).toarray()

X
y
#Now, we need to split our data into training and test sets.

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
print("X_train ---------->\n", X_train, "\nX_test -------->\n", X_test)

#PCA used
from sklearn.decomposition import PCA
pca = PCA(n_components = 100)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)
explained_variance = pca.explained_variance_ratio_

#Logistic Regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0, max_iter=1000)
classifier.fit(X_train, y_train)

#how our model performs on the test data
y_pred = classifier.predict(X_test)

#To calculate the accuracy of our model, the simplest way is to construct a confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm
