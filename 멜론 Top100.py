#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import urllib.request
from bs4 import BeautifulSoup


# In[2]:


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
req = requests.get('https://www.melon.com/chart/index.htm', headers = header) ## 주간 차트를 크롤링 할 것임
html = req.text


# In[3]:


soup = BeautifulSoup(html,'html.parser')
soup


# In[4]:


top100 = soup.find_all('div',class_='ellipsis rank01')


# In[5]:


top100


# In[6]:


top100 = [a.get_text().strip() for a in top100[:101]]


# In[7]:


top100


# In[8]:


singer =soup.find_all('div',class_="ellipsis rank02")
singer


# In[9]:


singer = [a.get_text().strip() for a in singer[:101]]


# In[10]:


singer


# In[11]:


singers = []
for i in singer:
    a = i[:int(len(i)/2)]
    singers.append(a)
singers


# In[14]:


for x,y in zip(top100,singers):
    print(x,y)


# In[ ]:




