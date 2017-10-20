
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

a = np.array([1, 2, 3])
a


# In[3]:

a.dtype


# In[4]:

np.array([1, 2, 3, 'b'])


# In[5]:

import scipy


# In[6]:

get_ipython().magic('matplotlib inline')

import matplotlib


# In[7]:

import pandas as pd


# In[8]:

pd.DataFrame


# In[9]:

# numero_de_banheiros,bairro,tem_farmacia_perto
# 2,Santa Clara,0
# 1,Santa Clara,1


# # Começando com Machine Learning

# Vamos usar o banco de dados de preços de casas de Boston para tentar predizer preços de novas casas.

# In[10]:

import pandas as pd


# In[11]:

from sklearn.datasets import load_boston


# In[15]:

boston = load_boston()


# In[16]:

print(boston['DESCR'])


# In[17]:

boston['data']


# In[18]:

boston['target']


# In[21]:

type(boston['data'])


# In[22]:

data = pd.DataFrame(boston.data)


# In[23]:

data


# In[24]:

from sklearn import linear_model


# In[36]:

from sklearn.cross_validation import train_test_split


# In[37]:

X_train, X_test, y_train, y_test =     train_test_split(
    X, y, test_size=0.3, random_state=0)


# In[38]:

reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)


# In[39]:

reg.predict([[40], [20], [2]])


# In[40]:

reg.score(X_test, y_test)


# In[42]:

get_ipython().magic('matplotlib inline')


# In[43]:

from altair import *


# In[44]:

Chart(data).mark_point().encode(
    x='0',
    y='price',
)


# In[45]:

Chart(data).mark_point().encode(
    x='9',
    y='price',
)


# In[46]:

X = data[[0, 9]]
y = data['price']


# In[47]:

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0)


# In[48]:

reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
reg.score(X_test, y_test)


# In[ ]:



