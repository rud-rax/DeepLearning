#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Regression Example With Boston Dataset: Standardized and Wider
from pandas import read_csv
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from scikeras.wrappers import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


# In[ ]:


# load dataset
dataframe = read_csv("housing.csv", delim_whitespace=True, header=None)
dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[:,0:13]
Y = dataset[:,13]


# In[ ]:


# define wider model
def wider_model():
 # create model
 model = Sequential()
 model.add(Dense(20, input_shape=(13,), kernel_initializer='normal', activation='relu'))
 model.add(Dense(1, kerne


# In[ ]:


# Compile model
model.compile(loss='mean_squared_error', optimizer='adam')
return model


# In[ ]:


# evaluate model with standardized dataset
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasRegressor(model=wider_model, epochs=100, batch_size=5, verbose=0)))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10)
results = cross_val_score(pipeline, X, Y, cv=kfold, scoring='neg_mean_squared_error')
print("Wider: %.2f (%.2f) MSE" % (results.mean(), results.std


# In[ ]:




