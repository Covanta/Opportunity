#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pyxlsb import open_workbook as open_xlsb


# In[3]:


#File Read
df1=pd.read_excel('C:/Users/clink/OneDrive - Covanta/Desktop/2021 Database.xlsx',sheet_name='Data')
df2=pd.read_excel('C:/Users/clink/OneDrive - Covanta/Desktop/2022 Database.xlsx',sheet_name='Data')
df3=pd.read_excel('C:/Users/clink/OneDrive - Covanta/Desktop/2023 Database July YTD.xlsx',sheet_name='Data')


# In[4]:


df2.drop(['Unnamed: 23', 'Unnamed: 24'],axis=1,inplace=True)


# In[5]:


#df3.drop(['Concatenate - Customers Existing in 2022', 'CS Check'],axis=1,inplace=True)


# In[6]:


F7=pd.concat([df2,df3])


# In[7]:


F7.columns


# In[8]:

#F7['Logic']=F7['Item']+F7['Customer Clean'] Original code.  Altered to meet new requirements
F7['Logic']=F7['LOB']+F7['Generator Name']
F7['Logic']=F7['Logic'].str.upper()


# In[9]:


F7['Date']=pd.to_datetime(F7['Date'])
F7['year']=F7['Date'].dt.year
F7['month']=F7['Date'].dt.month


# In[10]:


recent_year = 2023
df_recent =F7[F7['year'] == recent_year]


# In[11]:


recent_generator_names = set(df_recent['Logic'])


# In[12]:


previous_years = [2022]
df_previous = F7[F7['year'].isin(previous_years)]


# In[13]:


previous_generator_names = set(df_previous['Logic'])


# In[14]:


unique_generator_names = recent_generator_names - previous_generator_names


# In[15]:


unique_generator_names_list = list(unique_generator_names)


# In[16]:


list=sorted(unique_generator_names_list)


# In[17]:


list


# In[18]:


df=F7[F7['Logic'].isin(list)]


# In[19]:


dff=df[df['Customer Clean'].isin(df1['Customer Clean'])]



# In[20]:


dff


# In[21]:


dff['Amount'].sum()


# In[22]:


dff=dff.assign(Initiative=['Cross Sell']*len(dff))


# In[23]:


dff.to_csv('C:/Users/clink/OneDrive - Covanta/Desktop/cross_sell_23_new2.csv', index=False)


# In[ ]:




