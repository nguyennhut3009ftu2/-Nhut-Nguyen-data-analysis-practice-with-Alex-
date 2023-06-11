#!/usr/bin/env python
# coding: utf-8

# # EDA with Pandas

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib as plt


# In[16]:


#Read csv file from file path
df = pd.read_csv(r"C:\Users\nhut.nguyen\Downloads\world_population.csv")


# In[17]:


#See the info of each columns & its datatype
df.info()


# In[27]:


pd.set_option('display.float_format', lambda x: '%.2f' % x)


# In[28]:


#Check null value
df.isnull().sum()


# In[29]:


df.describe(include ='all')


# In[30]:


df.nunique()


# In[31]:


df.sort_values(by='Area (km²)', ascending = False)


# In[33]:


#Check the correlation of each variable
df.corr()


# In[42]:


#Show the correlation by using heatmap seaborn
sns.heatmap(df.corr(), annot=True)
plt.rcParams['figure.figsize']=(20,7)


# ### Group Data

# In[44]:


#Group data by 'Continent' and use mean value
df1 = df.groupby('Continent').mean()
df1


# In[47]:


df_oceania = df[df['Continent']=='Oceania']
df_oceania


# In[70]:


df2 = df1.sort_values(by='2022 Population', ascending=False)
df2 = df2[['1970 Population', '1980 Population', '1990 Population',
       '2000 Population', '2010 Population', '2015 Population',
       '2020 Population', '2022 Population']]
df2


# In[71]:


df2 = df2.transpose()


# In[69]:


df1.columns


# ## Visualize Grouped Data

# In[72]:


df2.plot()


# In[73]:


#Boxplots for outliers
df.boxplot(figsize=(20,10))


# # Data Types of columns

# In[75]:


df.dtypes


# In[76]:


#Select only numeric value in df
df.select_dtypes('number')


# In[77]:


#Select only object value in df
df.select_dtypes('object')


# In[ ]:




