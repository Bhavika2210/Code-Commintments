# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:22:22 2021

@author: Dell
"""
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
data_income=pd.read_csv("C:/Users/Dell/OneDrive/Desktop/income(1).csv")
data=data_income.copy()
data.info()
data.isnull().sum()
data.describe()
summary_cate=data.describe(include="O")
print(summary_cate)
data['JobType'].value_counts() # tells the no. of entries per column
data['occupation'].value_counts()
# to get to know about the question marks:
np.unique(data['JobType'])
np.unique(data['occupation'])
# notice a space before a question mark
# We read the data again and consider " ?" as nan
data=pd.read_csv("C:/Users/Dell/OneDrive/Desktop/income(1).csv",na_values=[" ?"])
data.isnull().sum()
# Now we need to check for those rows whose atleast one column is missing
missing=data[data.isnull().any(axis=1)]
data.isnull().sum()
# this means that 1809 are nan in jobtype and 1816 are nan in occupation. 7 have never worked,

data2=data.dropna(axis=0) ## we are dropping all the rows of data
correlation=data2.corr() # Helps to establish relation between independent variables
# ^ none of the values are close to 1, which means they dont have much of a correlation
# we look at the categories to check for any relation
data2.columns
# to check the distribution of gender :
gender=pd.crosstab(index=data2['gender'], normalize=True, columns='countHELLO')
# to check relation between gender and salary status: we make a two way table 
gender_salary=pd.crosstab(index=data2['gender'],columns=data2["SalStat"], margins=True, normalize=True)
gender_salary=pd.crosstab(index=data2['gender'],columns=data2["SalStat"], margins=True, normalize='index')
sal_stat=sns.countplot(data2["SalStat"])
sns.distplot(data2['age'],bins=10,kde=True)
sns.boxplot('age','SalStat', data=data2)
'''data2.groupby('SalStat')['age'].median()
plt.bar(x=data2['JobType'],data2['SalStat'],color=['blue','yellow'])
plt.title('Age vs Salary status')
plt.show()'''

cross2=pd.crosstab(index=data2['SalStat'],columns=data2['JobType'],normalize=True,margins=True)

#categorizing 
data2["SalStat"]=data2['SalStat'].map({' less than or equal to 50,000':0,' greater than 50,000':1})
print(data2["SalStat"])

new_data=pd.get_dummies(data2,drop_first=False)
sns.distplot(data2['capitalgain'],bins=10,kde=False)
column_list=list(new_data.columns)
#to exclude dependent variable salstat
features=list(set(column_list)-set(['SalStat']))
y=new_data["SalStat"].values
x=new_data[features].values
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.3,random_state=0)


logistic=LogisticRegression()
logistic.fit(train_x,train_y)
logistic.coef_
logistic.intercept_
#MODEL READY !
prediction=logistic.predict(test_x)
conf=confusion_matrix(test_y,prediction)
# less than or equal to 50k : 6270 right, 553 wrong
#greeater than 50k: 905 wrong, 1321 right . The principal diagonal tells us what is right 
#to find accuracy of our model
accuracy=accuracy_score(test_y,prediction)
# 83.88 % accurate
wrong=(test_y!=prediction).sum()
print(wrong) # 1458 misclassifications
#now we try to improve the accuracy of the model by dropping the irrelevant columns
#reindexing
data2["SalStat"]=data2["SalStat"].map({" less than or equal to 50,000":0," greater than 50,000":1})

notrequired=['gender','nativecountry','race','JobType']
new_data=data2.drop(notrequired,axis=1)
new_data=pd.get_dummies(data2,drop_first=True)
col_list=list(new_data.columns)
features=list(set(col_list)-set("SalStat"))
x=new_data[features].values
y=new_data["SalStat"].values
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.3,random_state=0)
logistic2=LogisticRegression()
logistic2.fit(train_x,train_y)
logistic2.intercept_
logistic2.coef_

#model ready
prediction2=logistic2.predict(test_y,prediction2)
conf2=confusion_matrix(test_y,prediction2)
accuracy2=accuracy_score(test_y,prediction2)
