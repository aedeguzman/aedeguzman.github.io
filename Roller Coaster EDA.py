#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis w/ Roller Coaster  Data Set 

# ### Upload Libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option("display.max_columns", 200)


# In[2]:


df = pd.read_csv('coaster_db.csv')


# ### Data Understanding

# In[3]:


df.shape #1087 rows, 56 columns


# In[4]:


df.head()


# In[5]:


df.columns #list all columns


# In[6]:


df.dtypes #check what type each column is


# In[7]:


df.describe()


# ### Data Preparation

# In[8]:


df.head()


# In[9]:


df = df[['coaster_name',  #Removing un-needed columns
    #'Length', 'Speed', 
     'Location', 'Status', 
    #'Opening date',
     #'Type', 
     'Manufacturer', 
     #'Height restriction', 'Model', 'Height',
       #'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
       #'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
       #'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
       #'Track layout', 'Fastrack available', 'Soft opening date.1',
       #'Closing date', 
     #'Opened', 
     #'Replaced by', 'Website',
       #'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
       #'Single rider line available', 'Restraint Style',
       #'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
       'year_introduced', 
         'latitude', 'longitude', 
         'Type_Main',
       'opening_date_clean', 
     #'speed1', 'speed2', 'speed1_value', 'speed1_unit',
       'speed_mph', 
     #'height_value', 'height_unit', 
     'height_ft',
       'Inversions_clean', 'Gforce_clean']].copy() #Let's Python know it's a new df and not referencinng the old one


# In[ ]:


# Exampleof dropping single column
# df.drop(['Column Name'], axis =1 )


# In[10]:


df.shape


# In[11]:


pd.to_datetime(df['opening_date_clean']) #change dtype from object to datetime


# In[ ]:


#pd.to_numeric(df['year_introduced'])change dtype to numeric


# #### Rename our columns

# In[12]:


df = df.rename(columns={'coaster_name': 'Coaster_Name',
                  'year_introduced': 'Year_Introduced',
                  'opening_date_clean': 'Opening_Date',
                  'speed_mph': 'Speed_mph',
                  'height_ft': 'Height_ft',
                  'inversions_clean': 'Inversions',
                  'Gforce_clean': 'Gforce'})


# In[13]:


df.head()


# In[14]:


df.columns


# In[15]:


df.isna().sum() # Check for NULL values


# In[16]:


df.loc[df.duplicated()] # Check for duplicates


# In[17]:


df.loc[df.duplicated(subset=['Coaster_Name'])].head()


# In[18]:


#Checking an example of duplicate
df.query("Coaster_Name=='Crystal Beach Cyclone'")


# In[19]:


df.columns


# In[20]:


# Drop duplicated columns
df = df.loc[~df.duplicated(subset=['Coaster_Name','Location','Opening_Date'])] .reset_index(drop = True ).copy() # reset order of data in table


# In[21]:


df.shape


# In[22]:


df.shape


# In[23]:


#zCounys how many unique values occur
ax = df['Year_Introduced'].value_counts().head(10) .plot(kind = 'bar', title = 'Top 10 Years Coasters Introduced')
ax.set_xlabel('Year Introduced')
ax.set_ylabel('Count')


# In[24]:


ax = df['Speed_mph'].plot(kind = 'hist', 
                          bins = 20, 
                          title = 'Coaster Speed (mph)')
ax.set_xlabel('Speed (mph)')


# In[25]:


ax = df['Speed_mph'].plot(kind = 'kde', #kernel density plot 
                          title = 'Coaster Speed (mph)')
ax.set_xlabel('Speed (mph)')


# ### Feature Relationships

# In[ ]:


df


# In[28]:


df.plot(kind = 'scatter', x = 'Speed_mph', y = 'Height_ft', title = 'Coaster Speed vs. Height')
plt.show()


# In[29]:


sns.scatterplot(x = 'Speed_mph', 
                y = 'Height_ft', 
                hue = 'Year_Introduced', 
                data = df)


# In[33]:


sns.pairplot(df, vars = ['Year_Introduced', 'Speed_mph', 'Height_ft', 'Inversions_clean', 'Gforce'], hue = 'Type_Main')
plt.show()


# In[34]:


df_corr = df[['Year_Introduced', 'Speed_mph', 'Height_ft', 'Inversions_clean', 'Gforce']].dropna().corr() #Show correlation
df_corr


# In[35]:


sns.heatmap(df_corr, annot = True)


# ### Ask a Question About the Data

# What location has the fastests roller coasters (minimum of 10 coasters)?

# In[36]:


df['Location']


# In[37]:


ax = df.query('Location != "Other"').groupby('Location')['Speed_mph'].agg(['mean','count']).query('count >=10').sort_values('mean')['mean'].plot(kind = 'barh',figsize = (12, 5), title = 'Average coaster Speed by Location')
ax.set_xlabel('Average Coaster Speed')
       


# In[38]:


df.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




