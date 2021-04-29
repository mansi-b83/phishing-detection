#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier


# In[2]:


# reading csv file,creating dataframes and shuffling dataframe rows to train the model and displaying first five rows of dataframe
df = pd.read_csv(r'C:\Users\Mansi\rdbms_IA2\dataset.csv',index_col=0) #read csv file to create pandas dataframe
df = sklearn.utils.shuffle(df) #to shuffle rows of dataframe created
X = df.drop("Result",axis=1).values #drops results column from shuffled data
X = preprocessing.scale(X) #scale the spread out data to lower the bias
y = df['Result'].values
df.head() #returns first 5 rows of dataframe


# In[3]:


#create dictionary for accuracy,precision,recall and f1 score
cal_score = {'accuracy': 'accuracy',
        'recall': 'recall',
        'precision': 'precision',
        'f1': 'f1'}
fold_count=10 #number of folds to split dataset into
def mean_score(scoring):
    return {i:j.mean() for i,j in scoring.items()}


# In[4]:


#for evaluating decision tree classifier
dtree_clf=DecisionTreeClassifier()
cross_val_scores = cross_validate(dtree_clf,X,y, cv=fold_count, scoring=cal_score) # cross validate data and calculate performance
dtree_score = mean_score(cross_val_scores)# calculate mean of cross validate result
print(dtree_score)
   


# In[5]:


#for evaluating Random Forest Classifier
rforest_clf=RandomForestClassifier()
cross_val_scores = cross_validate(rforest_clf, X, y, cv=fold_count, scoring=cal_score) #cross validate data and calculate performance
rforest_clf_score = mean_score(cross_val_scores) #calculate mean of cross validate result
print(rforest_clf_score)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




