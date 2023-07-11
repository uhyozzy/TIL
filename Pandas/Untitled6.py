#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[6]:


train_data=pd.read_csv("C:/Users/YHJ/Desktop/data/train.csv",
                      index_col='PassengerId',
                      usecols=['PassengerId','Survived','Name','Sex','Age'])
train_data.head()


# In[8]:


data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2000002],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율":[0.0283, 0.0163, 0.0982,0.0141]
}
df3=pd.DataFrame(data)
df3


# In[9]:


print(df3.columns)
type(df3.columns)


# In[39]:



index=['서울','부산','인천','대구']
df3=pd.DataFrame(data,index=index)
df3.index.name='도시'
df3.columns.name='특성'
df3


# In[11]:


train_data.head()


# In[19]:


train_data.size

train_data.shape


# In[20]:


train_data.info()


# In[21]:


train_data.describe()


# In[29]:


df3


# In[32]:


df3['2010-2015 증가율']*100


# In[47]:


df3['2010-2015 증가율']=df3['2010-2015 증가율']*100


# In[34]:


df3['2010-2015 증가율']


# In[40]:


df3['비고']=['특별시','광역시','특례시','특례시']
df3


# In[41]:


del df3['비고']
df3


# In[48]:


df3['2005-2015 증가율']=((df3['2015']-df3['2005'])/df3['2005']*100).round(2)
df3


# In[49]:


del df3['2005-2015 증가율']
df3


# In[51]:


df3.loc['광주']=['호남권',2470000,2456000,2453000,2460000,1.00]
df3


# In[54]:


df3.지역


# In[55]:


df3[['지역']]


# In[56]:


df3[['2010','2015']]


# In[58]:


df5=pd.DataFrame(np.arange(12).reshape(3,4))
df5


# In[61]:


np.arange(12).reshape(3,4)


# In[62]:


df3


# In[63]:


df3[:'서울']


# In[64]:


df3['서울':'인천']


# In[80]:


df3[['2015']][:'서울']


# In[81]:


df3


# In[82]:


df3.drop(index=['광주'])


# In[85]:


df3=df3.drop(index=['광주'])
df3


# In[87]:


df3.drop(columns=['2010-2015 증가율','2010'])


# In[91]:


df3.drop(['대구'],axis=0)

