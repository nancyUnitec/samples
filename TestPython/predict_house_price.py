#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 13:48:49 2017

@author: lc4
"""
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

# Function to get data
def get_data(file_name):
 data = pd.read_csv(file_name)
 X_parameter = []
 Y_parameter = []
 #for single_square_feet ,single_price_value in zip(data['square_feet'],data['price']):
 for single_square_feet ,single_price_value in zip(data['claimPeriod'],data['LR']):
       X_parameter.append([float(single_square_feet)])
       Y_parameter.append(float(single_price_value))
 return X_parameter,Y_parameter

# Function for Fitting our data to Linear model
def linear_model_main(X_parameters,Y_parameters,predict_value):
 # Create linear regression object
 regr = linear_model.LinearRegression()
 regr.fit(X_parameters, Y_parameters)
 predict_outcome = regr.predict(predict_value)
 predictions = {}
 predictions['intercept'] = regr.intercept_
 predictions['coefficient'] = regr.coef_
 predictions['predicted_value'] = predict_outcome
 return predictions

X,Y = get_data('input_data.csv')
predictvalue = 7
result = linear_model_main(X,Y,predictvalue)
print ("Intercept value " , result['intercept'])
print ("coefficient" , result['coefficient'])
print ("Predicted value: ",result['predicted_value'])
"""
import numpy as np


#%matplotlib inline

##############no work############
"""
import matplotlib.pyplot as plt
from pylab import *


income = [3 4 5 5];
outgo = [2.5 4.0 3.35 4.9];

subplot(2,1,1); plot(income)
subplot(2,1,2); plot(outgo)
"""
####################################


############draw a sin curve#############
"""
x = np.arange(-5.0, 5.0, 0.02)
y1 = np.sin(x)

plt.figure(1)

#subplot is a matlab function
#(211) means 2 lines multiply 1 column, and the position is 1
plt.subplot(211)
plt.plot(x, y1)

plt.subplot(212)
#设置x轴范围
xlim(-2.5, 2.5)
#设置y轴范围
ylim(-1, 1)
plt.plot(x, y1)
"""
#############################################