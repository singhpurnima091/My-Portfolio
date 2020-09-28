#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


#Import data into python environment


# In[2]:


com_data ='~/Documents/Comcast_telecom_complaints_data.csv'


# In[3]:


com_data1=pd.read_csv(com_data)


# In[4]:


com_data1


# In[5]:


x1=com_data1.Date
y=com_data1.Date.value_counts()


# In[6]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


x1


# In[8]:


y


# In[9]:


com_data1.Date


# In[10]:


plt.figure(figsize = (15,10))
plt.plot(com_data1.Date.value_counts())
plt.show()


# In[86]:


#Provide the trend chart for the number of complaints at monthly and daily granularity levels
y1 = com_data1.Date.value_counts()
y1


# In[12]:


plt.figure(figsize = (15,10))
y1.plot.bar()
plt.show


# In[34]:


import datetime


# In[65]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:





# In[13]:


f=com_data1['Customer Complaint']
f1=f.value_counts()


# In[14]:


f


# In[15]:


f1


# In[62]:


plt.figure(figsize = (15,10))
f1.plot.bar()
plt.show


# In[88]:


# Which complaint types are maximum i.e.,around internet,network issues, or across any other domains
c=com_data1['Customer Complaint']
c1=c.value_counts()


# In[91]:


c1.max()


# In[17]:


c1


# In[21]:





# In[18]:


freq_table = pd.crosstab(com_data1["Customer Complaint"],  
                              columns="count") 


# In[19]:


freq_table


# In[ ]:


#Provide the trend chart for the number of complaints at monthly and daily granularity levels


# In[20]:


freq_table1 = pd.crosstab(com_data1["Date"],  
                              columns="count") 


# In[21]:


freq_table1


# In[22]:


plt.figure(figsize = (20,15))
freq_table1.plot.bar()
plt.show


# In[83]:


max_complaint=pd.crosstab(com_data1["Customer Complaint"],  
                   columns="count")
max_complaint


# In[85]:


plt.figure(figsize = (10,5))
max_complaint.plot.bar()
plt.show


# In[23]:


max=com_data1['Customer Complaint'].value_counts()
max


# In[24]:


plt.figure(figsize = (15,10))
max.plot.bar()
plt.show


# In[51]:


com_data1


# In[ ]:


# Create a new categorical variable with value as Open and Closed. Open & Pending is to be categorized as Open and Closed &
#Solved is to be categorized as Closed


# In[56]:


import numpy as np


# In[57]:


com_data1['Status_New'] = np.where( (com_data1['Status']=='Open') | (com_data1['Status']=='Pending'), 'Open', 'Closed')


# In[58]:


com_data1


# In[92]:


# Provide state wise status of complaints in a stacked bar chart. Use the categorized variable from Q3.


# In[59]:


pd.crosstab(com_data1.State, com_data1.Status_New).plot.bar(figsize = (15,5), stacked = True)
plt.xticks(rotation = 0)
plt.legend(loc = 'upper left')
plt.show()


# In[93]:


# Which state has the maximum complaints


# In[60]:


freq_table2 = pd.crosstab(com_data1["State"],  
                              columns="count") 


# In[61]:


freq_table2


# In[94]:


# Which state has the highest percentage of unresolved complaints
# Provide the percentage of complaints resolved till date, which were received through the Internet and customer care calls


# In[62]:


pd.crosstab(com_data1.State,com_data1.Status_New,margins=True)


# In[87]:


#Provide the trend chart for the number of complaints at monthly and daily granularity levels


# In[72]:


com_data1.dtypes


# In[73]:


com_data1['Date_month_year']=pd.to_datetime(com_data1.Date_month_year)


# In[74]:


com_data1.dtypes


# In[ ]:


location = list(com_data1.columns).index('Date_month_year') + 1


# In[76]:


com_data1.insert(location, 'Month', (com_data1.Date_month_year.dt.month))


# In[77]:


com_data1


# In[78]:


freq_table3 = pd.crosstab(com_data1["Month"],  
                              columns="count") 


# In[79]:


freq_table3


# In[80]:


plt.figure(figsize = (20,15))
freq_table3.plot.bar()
plt.show


# In[ ]:




