# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 15:39:50 2017

@author: Jason Livingston
"""

##R-Squared of two arrays/lists/pandas DF columns
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

## After importing an SKlearn predictive model, Returning adjusted R-Squared. Intended for regression problems.
## Can be adapted to return model coefficients/projections along with R-Squared
def adjustedrsquaredfn(model, training_data, target_data):
    import pandas as pd
    import numpy as np
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