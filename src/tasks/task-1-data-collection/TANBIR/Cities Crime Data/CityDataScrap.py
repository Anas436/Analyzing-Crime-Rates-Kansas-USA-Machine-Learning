#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import requests
from bs4 import BeautifulSoup
url= 'https://www.city-data.com/crime/crime-Overland-Park-Kansas.html'
page = requests.get(url)


# In[3]:


soup = BeautifulSoup(page.text, 'lxml')


# In[4]:


soup


# In[9]:


table1 = soup.find('table', id='crimeTab')
headings=[]
for j in table1.find_all('h4'):
    headings.append(j.text)
    print(headings)


# In[10]:


body=[]
for i in table1.find_all('tr')[1:]:
   row_data = i.find_all('td')
   row = [i.text for i in row_data]
   body.append(row)


# In[11]:


city1=pd.DataFrame(body, columns=headings)


# In[12]:


print(city1)


# In[14]:


city1.to_csv('City1_data.csv', index=False)


# In[ ]:




