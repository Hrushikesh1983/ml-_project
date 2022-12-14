# -*- coding: utf-8 -*-
"""PREM's ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17dc1kH7re52kLpqA8SxaOaXne3WmihHT
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("https://raw.githubusercontent.com/Premalatha-success/Datasets/main/hotel_bookings.csv")
data.head(5)

data.shape

data.dtypes

correlation_mat = data.corr()

sns.heatmap(correlation_mat,annot=True,linewidths=.5,cmap="YlGnBu")

data.isnull().sum()

plt.figure(figsize=(10,6))
sns.heatmap(data.isnull(),yticklabels=False)

data.drop("company", axis=1,inplace=True)
data.info()

plt.figure(figsize=(10,6))
sns.heatmap(data.isnull(),yticklabels=False)

data["agent"].value_counts()

data["agent"].replace(np.nan, data["agent"].median(), inplace=True)

data["country"].value_counts()

data["country"].replace(np.nan, data["country"].mode().values[0], inplace=True)

data["children"].replace(np.nan, data["children"].median(), inplace=True)

plt.figure(figsize=(10,6))
sns.heatmap(data.isnull(),yticklabels=False)

from sklearn.preprocessing import LabelEncoder
lencode = LabelEncoder()
data["hotel"] = lencode.fit_transform(data["hotel"])
data["arrival_date_month"] = lencode.fit_transform(data["arrival_date_month"])
data["meal"] = lencode.fit_transform(data["meal"])
data["country"] = lencode.fit_transform(data["country"])
data["market_segment"] = lencode.fit_transform(data["market_segment"])
data["distribution_channel"] = lencode.fit_transform(data["distribution_channel"])
data["reserved_room_type"] = lencode.fit_transform(data["reserved_room_type"])
data["assigned_room_type"] = lencode.fit_transform(data["assigned_room_type"])
data["deposit_type"] = lencode.fit_transform(data["deposit_type"])
data["customer_type"] = lencode.fit_transform(data["customer_type"])
data["reservation_status"] = lencode.fit_transform(data["reservation_status"])
data["reservation_status_date"] = lencode.fit_transform(data["reservation_status_date"])

data.info()

data.head(5)

X = data.drop(["is_canceled"], axis=1)
y = data["is_canceled"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=0)

from sklearn.linear_model import LogisticRegression
model1=LogisticRegression(solver="liblinear")
model1.fit(X_train,y_train)
model1.score(X_train,y_train)

model1.score(X_test,y_test)

from sklearn.tree import DecisionTreeClassifier 
dtree=DecisionTreeClassifier(criterion="gini")
dtree.fit(X_train,y_train)

dtree.score(X_train,y_train)

dtree.score(X_test,y_test)

dTreeR = DecisionTreeClassifier(criterion = 'gini', max_depth = 3, random_state=0)
dTreeR.fit(X_train, y_train)
print(dTreeR.score(X_train, y_train))

y_predict = dTreeR.predict(X_test)
y_predict

print(dTreeR.score(X_test, y_test))

from sklearn import metrics
cm=metrics.confusion_matrix(y_test, y_predict,labels=[0, 1])

df_cm = pd.DataFrame(cm, index = [i for i in ["No","Yes"]],
                  columns = [i for i in ["No","Yes"]])
plt.figure(figsize = (7,5))
sns.heatmap(df_cm, annot=True ,fmt='g')

from sklearn.ensemble import BaggingClassifier
bgcl = BaggingClassifier( n_estimators=150,base_estimator=dTreeR,random_state=0)
bgcl = bgcl.fit(X_train,y_train)
y_predict = bgcl.predict(X_test)
print(bgcl.score(X_test,y_test))

from sklearn import metrics
cm=metrics.confusion_matrix(y_test, y_predict,labels=[0, 1])

df_cm = pd.DataFrame(cm, index = [i for i in ["No","Yes"]],
                  columns = [i for i in ["No","Yes"]])
plt.figure(figsize = (7,5))
sns.heatmap(df_cm, annot=True ,fmt='g')

from sklearn.ensemble import AdaBoostClassifier
acl = AdaBoostClassifier(n_estimators = 120,random_state=0)
acl = acl.fit(X_train, y_train)
y_predict = acl.predict(X_test)
print(acl.score(X_test, y_test))

from sklearn.ensemble import GradientBoostingClassifier
jbl = GradientBoostingClassifier(n_estimators = 200,random_state=0)
jbl = jbl.fit(X_train, y_train)
y_predict = jbl.predict(X_test)
print(jbl.score(X_test, y_test))

cm=metrics.confusion_matrix(y_test, y_predict,labels=[0, 1])

df = pd.DataFrame(cm, index = [i for i in ["No","Yes"]],
                  columns = [i for i in ["No","Yes"]])
plt.figure(figsize = (7,5))
sns.heatmap(df_cm, annot=True ,fmt='g')

from sklearn.ensemble import RandomForestClassifier
rcl = RandomForestClassifier(n_estimators = 160, random_state=0,max_features=3)
rcl = rcl.fit(X_train, y_train)

y_predict = rcl.predict(X_test)
print(rcl.score(X_test, y_test))
cm=metrics.confusion_matrix(y_test, y_predict,labels=[0, 1])

df_cm = pd.DataFrame(cm, index = [i for i in ["No","Yes"]],
                  columns = [i for i in ["No","Yes"]])
plt.figure(figsize = (7,5))
sns.heatmap(df_cm, annot=True ,fmt='g')