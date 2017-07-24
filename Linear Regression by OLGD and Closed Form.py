# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:52:46 2017

@author: Jason Livingston
"""

import pandas as pd
import numpy as np
from sklearn import linear_model

##CLOSED FORM LINEAR REGRESSION
X = pd.DataFrame()
X['int'] = [1,1,1,1,1]
X['A'] = [1,2,3,4,5]
X['B'] = [3,4,4,6,7]


X = X.values
Y = [4,5,7,7,9]
#Y = Y.values

Xt=X.transpose()

XtX=np.dot(Xt,X)
XtY = np.dot(Xt,Y)
XtXinv = np.linalg.inv(XtX)
B = np.dot(XtXinv,XtY)

##SKLEARN LINEAR REGRESSION FOR COMPARISON
X = pd.DataFrame()
X['A'] = [1,2,3,4,5]
X['B'] = [3,4,4,6,7]

explin = linear_model.LinearRegression(fit_intercept = True)
explin.fit(X,Y)
explin.coef_

##ONLINE GRADIENT DESCENT
def predict(row,coefficients):
    row = row
    yhat = coefficients[0]
    for i in range(len(row) - 1):
        yhat = yhat+coefficients[i+1]*row[i]
    return yhat

def df_to_list_of_lists(df):
    df2 = []
    for i in range(len(df[list(df.columns.values)[0]])):
        templist = []
        for col in list(df.columns.values):
            x = df[col][i]
            templist.append(x)
        df2.append(templist)
    return df2
    
def coefficients_sgd(train,l_rate,n_epoch):
    if type(train) == pd.core.frame.DataFrame:
        train = df_to_list_of_lists(train)
    coefs = [0 for i in range(len(train[0]))]
    for epoch in range(n_epoch):
        for row in train:
            yhat = predict(row,coefs)
            error = yhat - row[-1]
            coefs[0] = coefs[0] - l_rate*error
            for i in range(len(row)-1):
                coefs[i+1] = coefs[i+1]-l_rate*error*row[i]
    return coefs

X = pd.DataFrame()
#X['int'] = [1,1,1,1,1]
X['A'] = [1,2,3,4,5]
X['B'] = [3,4,4,6,7]
X['Y'] = Y
coefficients = coefficients_sgd(train = X,l_rate = .001,n_epoch = 1000)
print("Intercept = %f Beta_A = %f Beta_B = %f"%tuple(coefficients) )
