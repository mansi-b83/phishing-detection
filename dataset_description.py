#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:


df = pd.read_csv(r'C:\Users\Mansi\rdbms_IA2\dataset.csv',index_col=0)#to read csv file
df.shape #shape of dataset i.e number of rows and columns in csv file


# In[3]:


df


# In[4]:


print("number of 1",len(df[df["Result"]==1])) #number of legitimate url
print("number of -1",len(df[df["Result"]==-1])) #number of phishing url


# In[5]:


corr=df.corr() #to find correlation among the features
corr


# In[6]:


#created a heatmap that shows correlation of the features
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(15, 15))#for layout and size

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, cmap=cmap, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})


# In[ ]:




