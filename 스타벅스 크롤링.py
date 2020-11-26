#!/usr/bin/env python
# coding: utf-8

# In[26]:


from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import time
import folium


# In[27]:


chrome_driver = 'C:/Users/BIT-R45/Downloads/chromedriver_win32 (1)/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver)

driver.get('https://www.istarbucks.co.kr/store/store_map.do')

loca = driver.find_element_by_class_name('loca_search')
loca.click()

sido = driver.find_element_by_class_name('sido_arae_box')
li = sido.find_elements_by_tag_name('li')
li[0].click()

time.sleep(1)

gugun = driver.find_element_by_class_name('gugun_arae_box')
guli = gugun.find_elements_by_tag_name('li')


guli[0].click()



# In[28]:


source = driver.page_source
bs = BeautifulSoup(source,'html.parser')
entire = bs.find_all('p',class_='result_details')
entires = [a.get_text().strip() for a in entire]


# In[23]:


entires


# In[29]:


data =bs.find_all('li',{'class':'quickResultLstCon'})
data


# In[30]:


len(data)


# In[31]:


wedo = []
for a in range(len(data)):
    x = data[a]['data-lat']
    wedo.append(x)
wedo


# In[32]:


kyoungdo=[]
for b in range(len(data)):
    x= data[b]['data-long']
    kyoungdo.append(x)
kyoungdo


# In[33]:


kyoungdo


# In[10]:


kyoungdo


# In[34]:


entires


# In[35]:


df =pd.DataFrame()


# In[36]:


df['위도']=wedo


# In[37]:


df['경도']=kyoungdo


# In[38]:


df


# In[39]:


df2 = df.apply(pd.to_numeric)


# In[40]:


df2['주소']=entires


# In[41]:


df2


# In[42]:


print(df2['위도'].mean())
print(df2['경도'].mean())


# In[79]:


map = folium.Map(location=[df2["위도"].mean(),df2["경도"].mean()],
                 zoom_start=12)


# In[80]:


map


# In[81]:


for i in df2.index:
    sub_lat= df2.loc[i,'위도']
    sub_long=df2.loc[i,'경도']
    
    folium.Marker([sub_lat,sub_long]).add_to(map)


# In[82]:


map


# In[83]:


map = folium.Map(location=[df2["위도"].mean(),df2["경도"].mean()],
                 zoom_start=12)
for i in df2.index:
    sub_lat= df2.loc[i,'위도']
    sub_long=df2.loc[i,'경도']
    color = 'green'
   
    folium.Marker([sub_lat,sub_long],color=color,radius = 5).add_to(map)


# In[84]:


map


# In[ ]:




