# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 10:25:21 2017

@author: Jason Livingston
"""

import pandas as pd
import numpy as np


#Credit to Jason Brownlee for inspiring descent method

def perceptron_fit(W0,lrate,iteration,data, sig_weight):
    w = W0
    lrate = lrate
    n = len(data)
    k = len(list(data.columns.values))
    e = iteration
    error = 0
    for a in range(e):
        for b in list(range(n)):
            z = 0
            for c in range(k-1):
                z = z+w[c]*data[list(data.columns.values)[c]][b]
            gz = 1/(1+(np.exp(-z)))
            oz = 1 if gz > sig_weight else 0
            error = (data[list(data.columns.values)[k-1]][b] - oz)
            for d in range(k-1):
                w[d] = w[d]+error*lrate*(data[list(data.columns.values)[d]][b])
    return(w)
            


def internal_neuron_out(W0,lrate,iteration,data, sig_weight):
    wnew = perceptron_fit(W0 = W0, lrate = lrate, iteration = iteration, data = data, sig_weight = sig_weight)
    k = len(list(data.columns.values))
    J = 0
    for a in range(k-1):
        J = J+data[list(data.columns.values)[a]]*wnew[a]
    J = np.array(J)
    gJ = 1/(1+np.exp(-J))
    #oz = np.where(gJ > .5,1, 0)
    return(gJ)

def neuron_out(W0,lrate,iteration,data, sig_weight):
    wnew = perceptron_fit(W0 = W0, lrate = lrate, iteration = iteration, data = data, sig_weight = sig_weight)
    k = len(list(data.columns.values))
    J = 0
    for a in range(k-1):
        J = J+data[list(data.columns.values)[a]]*wnew[a]
    J = np.array(J)
    gJ = 1/(1+np.exp(-J))
    oz = np.where(gJ > .5,1, 0)
    return(oz)
    
data = pd.DataFrame()
data['Bias'] = [1,1,1,1,1]
data['X1'] = [1,2,2,1,7]
data['X2'] = [1,1,4,4,7]
data['Y'] = [1,0,1,0,1] 

wnew = perceptron_fit(W0 = [0,0,0], lrate = .1, iteration = 50, data = data, sig_weight = .5)

n1 = neuron_out(W0 = [0,0,0], lrate = .1, iteration = 50, data = data, sig_weight = .1)
n2 = neuron_out(W0 = [0,0,0], lrate = .1, iteration = 50, data = data, sig_weight = .2)
n3 = neuron_out(W0 = [0,0,0], lrate = .1, iteration = 50, data = data, sig_weight = .3)
n4 = neuron_out(W0 = [0,0,0], lrate = .1, iteration = 50, data = data, sig_weight = .4)
n5 = neuron_out(W0 = [0,0,0], lrate = .1, iteration = 50, data = data, sig_weight = .5)
n6 = neuron_out(W0 = [0,0,0], lrate = .1, iteration = 50, data = data, sig_weight = .6)
n7 = neuron_out(W0 = [0,0,0], lrate = .1, iteration = 50, data = data, sig_weight = .7)
n8 = neuron_out(W0 = [0,0,0], lrate = .1, iteration = 50, data = data, sig_weight = .8)
n9 = neuron_out(W0 = [0,0,0], lrate = .1, iteration = 50, data = data, sig_weight = .9)


data_level_2 = pd.DataFrame()
data_level_2['bias'] = data['Bias']
data_level_2['n1'] = n1 
data_level_2['n2'] = n2
data_level_2['n3'] = n3
data_level_2['n4'] = n4
data_level_2['n5'] = n5
data_level_2['n6'] = n6
data_level_2['n7'] = n7 
data_level_2['n8'] = n8
data_level_2['n9'] = n9
data_level_2['Y'] = data['Y']

print(data_level_2)

h1 = neuron_out(W0 = [0,0,0,0,0,0,0,0,0,0], lrate = .1, iteration = 50, data = data_level_2, sig_weight = .525)
h2 = neuron_out(W0 = [0,0,0,0,0,0,0,0,0,0], lrate = .1, iteration = 50, data = data_level_2, sig_weight = .483)
h3 = neuron_out(W0 = [0,0,0,0,0,0,0,0,0,0], lrate = .1, iteration = 50, data = data_level_2, sig_weight = .518)


data_level_3 = pd.DataFrame()
data_level_3['bias'] = data['Bias']
data_level_3['h1'] = h1
data_level_3['h2'] = h2
data_level_3['h3'] = h3
data_level_3['Y'] = data['Y']

print(data_level_3)

out = neuron_out(W0 = [0,0,0,0], lrate = .1, iteration = 50, data = data_level_3, sig_weight = .5)
print(out)