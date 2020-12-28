#!/usr/bin/env python
# coding: utf-8

# In[1]:


# imports and load data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("store_data.csv")
df.head()


# In[2]:


df["week"] = pd.to_datetime(df["week"])
df.info()
df['Year'] = df['week'].dt.year
df["Month"] = df["week"].dt.month
df["Day"] = df["week"].dt.day
df.head()


# In[3]:


# explore data
x = df.loc[ : , : 'storeE']
sns.distplot(x["storeA"]);


# In[4]:


sns.distplot(x["storeB"]);


# In[5]:


sns.distplot(x["storeC"]);


# In[6]:


sns.distplot(x["storeD"]);


# In[7]:


sns.distplot(x["storeE"]);


# In[8]:


x.hist(figsize=(8, 8));
plt.show()


# In[9]:


# sales for the last month
filt = df["Year"] == df['Year'].max()
df[filt]
df[filt]["Month"].max()  


# In[10]:


# sales for the last month
filt = df["Year"] == df['Year'].max()
df_lastM = df[(df["Year"] == df["Year"].max()) & (df["Month"] == df[filt]["Month"].max()  )]
display(df_lastM.head())
display(df_lastM.head())
display(df_lastM.loc[ : , :"storeE"].describe())
display(df_lastM.loc[ : , :"storeE"].sum())


# In[11]:


# average sales
df.loc[ : , :"storeE"].mean()


# In[12]:


# sales for the week of March 13th, 2016
df.head()
df["Month_Name"] = df["week"].dt.month_name()
df.head()
df_lastW12 = df[(df["Month_Name"] == "March") & (df["Day"] == 13) & (df["Year"] == 2016)]
df_lastW12.head()
display(df_lastW12.head())
display(df_lastW12.loc[ : , :"storeE"].describe())
display(df_lastW12.loc[ : , :"storeE"].sum())


# In[13]:


# sales for the latest 3-month periods
df_last3M = df[df["week"] >= "2017-12-01"]
display(df_last3M.head())
display(df_last3M.loc[ : , :"storeE"].describe())
display(df_last3M.loc[ : , :"storeE"].sum())
display(df_last3M.loc[ : , :"storeE"].mean())


# In[ ]:




