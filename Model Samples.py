# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 10:07:21 2017

@author: Jason Livingston
"""
##Several SKlearn example fits with functions to quickly return fit, useful for determining the method which best describes the data (AR2)
import pandas as pd
import numpy as np
from treeinterpreter import treeinterpreter as ti
from sklearn import linear_model

data = pd.DataFrame(np.random.randint(0,100,size = (100,4)), columns = ['A','B','C','D'])

target = list(data['D'])
train = pd.DataFrame.copy(data.drop('D', axis = 1))

#Random Forest
forest = ti.RandomForestRegressor().fit(train,target)
forestpredict = forest.predict(train)

results = pd.DataFrame()
results['D'] = target
results['forest'] = forestpredict

#Linear Regression
linear = linear_model.LinearRegression().fit(train,target)
linearpredict = linear.predict(train)

results['linear'] = linearpredict

#Ridge Regression
ridge = linear_model.ridge.Ridge().fit(train,target)
ridgepredict = ridge.predict(train)

results['ridge'] = ridgepredict

#Baysian Ridge Regression
baysianridge = linear_model.BayesianRidge().fit(train,target)
baysianridgepredict = baysianridge.predict(train)

results['baysian ridge'] = baysianridgepredict

#Baysian Ridge Regression
logistic = linear_model.LogisticRegression().fit(train,target)
logisticpredict = logistic.predict(train)

results['logistic'] = logisticpredict

#MAPE Calculations
results['forest PE'] = abs(results['forest']-results['D'])/results['D']
results['linear PE'] = abs(results['linear']-results['D'])/results['D']
results['ridge PE'] = abs(results['ridge']-results['D'])/results['D']
results['baysian ridge PE'] = abs(results['baysian ridge']-results['D'])/results['D']
results['logistic PE'] = abs(results['logistic']-results['D'])/results['D']

forestMAPE = np.mean(results['forest PE'])
linearMAPE = np.mean(results['linear PE'])
ridgeMAPE = np.mean(results['ridge PE'])
baysianridgeMAPE = np.mean(results['baysian ridge PE'])
logisticMAPE = np.mean(results['logistic PE'])


def rsquaredfn(X,Y):
    import pandas as pd
    import numpy as np
    R = pd.DataFrame()
    R['X'] = X
    R['Y'] = Y
    MeanX = np.mean(R['X'])
    MeanY = np.mean(R['X'])
    R['A'] = R['X'] - MeanX
    R['B'] = R['Y'] - MeanY
    R['AXB'] = R['A']*R['B']
    R['A2'] = R['A']*R['A']
    R['B2'] = R['B']*R['B']
    AXB = np.sum(R['AXB'])
    A2 = np.sum(R['A2'])
    B2 = np.sum(R['B2'])
    correl = AXB/np.sqrt(A2*B2)
    rsquared = correl*correl
    return(rsquared)
    
forestR2 = rsquaredfn(results['D'],results['forest']) 
linearR2 = rsquaredfn(results['D'],results['linear']) 
ridgeR2 = rsquaredfn(results['D'],results['ridge']) 
baysianridgeR2 = rsquaredfn(results['D'],results['baysian ridge']) 
logisticR2 = rsquaredfn(results['D'],results['logistic']) 

def adjustedrsquaredfn(model, training_data, target_data):
    import pandas as pd
    lm = model()
    lm.fit(training_data,target_data)
    data = pd.DataFrame()
    data['Target'] = target_data
    data['Fit'] = lm.predict(training_data)
    MeanX = np.mean(data['Target'])
    MeanY = np.mean(data['Fit'])
    data['A'] = data['Target'] - MeanX
    data['B'] = data['Fit'] - MeanY
    data['AXB'] = data['A']*data['B']
    data['A2'] = data['A']*data['A']
    data['B2'] = data['B']*data['B']
    AXB = np.sum(data['AXB'])
    A2 = np.sum(data['A2'])
    B2 = np.sum(data['B2'])
    correl = AXB/np.sqrt(A2*B2)
    rsquared = correl*correl
    adjustedrsquared = 1-((1-rsquared)*(len(data['Target'])-1)/((len(data['Target'])-1)-len(list(training_data.columns.values))-1))
    return(adjustedrsquared)
    
forestAR2 = adjustedrsquaredfn(ti.RandomForestRegressor, train, target)
linearAR2 = adjustedrsquaredfn(linear_model.LinearRegression, train, target)
ridgeAR2 = adjustedrsquaredfn(linear_model.Ridge, train, target)
baysianridgeAR2 = adjustedrsquaredfn(linear_model.BayesianRidge, train, target)
logisticAR2 = adjustedrsquaredfn(linear_model.LogisticRegression, train, target)