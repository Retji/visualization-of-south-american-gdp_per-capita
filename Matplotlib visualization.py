#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use("ggplot")
get_ipython().run_line_magic('matplotlib.inline', '')


# In[28]:


gdp_data=pd.read_csv("C:\\Users\\Dakon\\Desktop\\Datasets\\Lesson 3\\north_america.csv") #to load the dataset from my local directory


# In[29]:


gdp_data.head() #viewing the first 5 rows of the dataset


# In[30]:


gdp_data.shape   #gives the number of rows and columns in the data


# In[63]:


countries=gdp_data["Country"]    #create a variable of countries 
colors=('g','b','y')


# In[64]:


year_2000=gdp_data["2000"]
year_2001=gdp_data["2001"]
year_2002=gdp_data["2002"]
year_2003=gdp_data["2003"]
year_2004=gdp_data["2004"]
year_2005=gdp_data["2005"]
year_2006=gdp_data["2006"]
year_2007=gdp_data["2007"]
year_2008=gdp_data["2008"]
year_2009=gdp_data["2009"]
year_2010=gdp_data["2010"]


# In[77]:


plt.figure(figsize=(4,4),dpi=120)
plt.pie(year_2000,labels=countries,colors=colors,
        shadow=True,
       wedgeprops={"edgecolor":"white"},
       startangle=90,
        explode=(0,0,0.07),
       autopct= "%1.1f%%",
        textprops={"fontsize":14},
       rotatelabels=True)
plt.tight_layout()
plt.show()


# In[ ]:




