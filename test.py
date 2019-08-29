# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
from model import predict
import pandas as pd
from sklearn import datasets
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.metrics import mean_squared_error


#%%
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']


#%%
da = pd.read_csv('validation.data')
db = pd.read_csv(url, names=names)


#%%
da.head()


#%%
db.head()


#%%


#%%


#%%
