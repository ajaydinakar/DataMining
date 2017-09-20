"""
Created on Tue Sep 19 20:29:40 2017

@author: Ajay Dinakar
"""
#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#importing the dataset
dataset=pd.read_csv("mortage_rates.csv")
x=dataset.iloc[:,0:1].values
y=dataset.iloc[:,1:2].values

#splitting the dataset into the training set and test set
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=0)

#fitting simple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)
#predicting test set results
y_pred=regressor.predict(x_test)
#visualising the training set results
plt.scatter(x_train,y_train,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title('Year vs Intrest Rates')
plt.xlabel('Year')
plt.ylabel('Interest Rate')
plt.show()

plt.scatter(x_test,y_test,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title('Year vs Intrest Rates')
plt.xlabel('Year')
plt.ylabel('Interest Rate')
plt.show()
