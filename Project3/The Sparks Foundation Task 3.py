#!/usr/bin/env python
# coding: utf-8

# # The Sparks Foundation
# ### GRIP Septemer 2021 Batch 
# ### Author: Teghpreet Singh Mago
# ### Task 3 : ‘Exploratory Data Analysis’ on dataset ‘Retail’

# ### 1. Problem defintion
# ● Perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’
# 
# ● As a business manager, try to find out the weak areas where you can work to make more profit.
# 
# ● What all business problems you can derive by exploring the data?
# ### 2. Dataset Source
# Data can be found at https://bit.ly/3i4rbWI
# ### 3. Evaluation
# If we can successfully express the data in the form of graphs and plots and derive appropriate conclusions, we'll be successful at the project.
# ### 4. Libraries and Features 
# For this project, we will import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns, warnings.

# ## Importing Libraries

# In[63]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# ## Importing Data in the form of CSV Files

# In[3]:


df = pd.read_csv(r'C:\Users\HP\Desktop\SampleSuperstore.csv')
df.head(15)


# In[7]:


print('The dimensions of the given dataset are', df.shape)


# In[11]:


df.describe().T


# In[14]:


print('Basic information ablout datatypes and cloumn values')
df.info()


# In[15]:


print('Columns that DO contain Null values are ')
df.isnull().sum()


# ## Reducing Data Redudancy

# In[24]:


print('Number of duplicate values present are', df.duplicated().sum())


# In[21]:


print('We will drop all the duplicate values from the columns and check for unique records')
df.drop_duplicates(inplace=True)

print('Number of duplicate values present now are', df.duplicated().sum())


# In[26]:


print('We shall print all columns with number of unique records in each column.')
df.nunique()


# ## Data Correction

# In[43]:


print('No we shall implement Data Correction')
df.corr()


# ## Extensive Data Visualisation

# ### Plot of Sales and Profit Density

# In[45]:


plt.figure(figsize=(8,8))
sns.kdeplot(df['Sales'],color='red',label='Sales',shade=True)
sns.kdeplot(df['Profit'],color='blue',label='Profit',shade=True)
plt.title('Plot of Sales and Profit Density',fontsize=20)
plt.xlabel('Sales and Profit',fontsize=15)
plt.ylabel('Densty',fontsize=15)
plt.xlim([-100,1000])
plt.legend()
plt.show()


# #### Conclusions and Predictions
# 1. The Profit aspect of the dataset showed greater variaion in density that the Sales Aspect.
# 2. From the Area Plot, the Sales Aspect is more widespread than the other.
# 3. Area Plot is a good representation of the Variability.
# 

# ### Plot of Seaborn Heatmap to show corelations between different columns

# In[62]:


sns.heatmap(df.corr(),cmap='cool',annot=True,linecolor='white',linewidth=2,cbar=False)


# #### Conclusions and Predictions
# 1. Sales and Profit are Moderately Correlated.
# 2. Discount and Profit are Negatively Correlated.
# 3. Quantity and sales are also correlated but less than moderate

# ### Plot of Seaborn Pairplot using Category paraeter

# In[95]:


sns.pairplot(df,hue='Category',palette='husl')


# ### Plot of Seaborn Pairplot using Region parameter

# In[93]:


sns.pairplot(df,hue='Region', palette='coolwarm')


# ### Plotting various Subplots for various parameters

# In[73]:


fig,axs=plt.subplots(nrows=2,ncols=2,figsize=(10,8));

#Plotting various subplots
sns.countplot(df['Category'],ax=axs[0][0], palette='Blues')
sns.countplot(df['Segment'],ax=axs[0][1], palette='Greens' )
sns.countplot(df['Ship Mode'],ax=axs[1][0], palette='Oranges')
sns.countplot(df['Region'],ax=axs[1][1], palette='Purples' )

#Setting titles for variouas subplots
axs[0][0].set_title('Category',fontsize=20)
axs[0][1].set_title('Segment',fontsize=20)
axs[1][0].set_title('Ship Mode',fontsize=20)
axs[1][1].set_title('Region',fontsize=20)

plt.tight_layout()
plt.show()


# ### Plotting Sub-Category Counts Plotted on a BarPlot

# In[205]:


plt.figure(figsize=(14,7))
sns.countplot(df['Sub-Category'], palette='pink')
plt.title('Sub-Category Counts Plotted on a BarPlot',fontsize=20)
plt.xticks(rotation = 60, fontsize=12.5)
plt.xlabel('Sub-category', fontsize=15)
plt.ylabel('Value Count', fontsize=15)
plt.grid(True)
plt.show()


# ### Plotting Bar Graph of State Counts 

# In[241]:


plt.figure(figsize=(14,7))
sns.countplot(df['State'])
plt.xticks(rotation=90, fontsize=13)
plt.xlabel('State', fontsize=15)
plt.ylabel('Value Count', fontsize=15)
plt.title('State Counts Plotted',fontsize=20)
plt.grid(True)
plt.show()


# ### Plotting various Subplots for various parameters

# In[242]:


fig, axs = plt.subplots(ncols=2, nrows = 2, figsize = (20,10))

sns.distplot(df['Sales'], color = 'blue',  ax = axs[0][0])
sns.distplot(df['Profit'], color = 'green',  ax = axs[0][1])
sns.distplot(df['Quantity'], color = 'orange',  ax = axs[1][0])
sns.distplot(df['Discount'], color = 'red',  ax = axs[1][1])

axs[0][0].set_title('Sales Distribution', fontsize = 20)
axs[0][1].set_title('Profit Distribution', fontsize = 20)
axs[1][0].set_title('Quantity distribution', fontsize = 20)
axs[1][1].set_title('Discount Distribution', fontsize = 20)
plt.tight_layout()
plt.show()


# ### Plotting Pie Chart of Statewise Dealings

# In[234]:


df1 = df.groupby(['State'])
states = df1['State'].count().sort_values(ascending=False)
print('Statewise Dealings are')
states


# In[240]:


plt.figure(figsize=(30,20))
plt.pie(states.head(30).values, labels = states.head(30).index, autopct = '%1.0f%%')
plt.legend(loc='best')
plt.title('State Wise Dealings of first 30 cities', fontsize = 20)
plt.show()


# In[237]:


m = df['State'].value_counts().mean()
print('The mean number of State Dealings are',m)
med = df['State'].value_counts().median()
print('The median number of State Dealings are',med)
max2 = df['State'].value_counts().max()
print('The maximum number of State Dealings are',max2)
min2 = df['State'].value_counts().min()
print('The minimum number of State Dealings are',min2)


# ### Plotting Pie Chart of Citywise Dealings 

# In[151]:


df1 = df.groupby(['City'])
cities = df1['City'].count().sort_values(ascending=False)
cities


# In[152]:


plt.figure(figsize=(25,25))
plt.pie(cities.head(30).values, labels = cities.head(30).index, autopct = '%1.0f%%')
plt.legend(loc='best')
plt.title('City Wise Dealings of first 30 cities', fontsize = 20)
plt.show()


# In[239]:


m = df['City'].value_counts().mean()
print('The mean number of City Dealings are',m)
med = df['City'].value_counts().median()
print('The median number of City Dealings are',med)
max2 = df['City'].value_counts().max()
print('The maximum number of City Dealings are',max2)
min2 = df['City'].value_counts().min()
print('The minimum number of City Dealings are',min2)


# ### Plotting Sales Vs Profit Bar Graph

# In[243]:


Sales = df.groupby('Region').sum()['Sales'].sort_values(ascending = False)
Profits = df.groupby('Region').sum()['Profit'].sort_values(ascending = False)

plt.figure(figsize=(10,8))
plt.bar(Sales.index, Sales.values, color = 'pink')
plt.bar(Profits.index, Profits.values, color='lightskyblue')
plt.xlabel('Regions',fontsize = 15)
plt.ylabel('Total sales & profit',fontsize = 15)
plt.title("Sales vs Profit",fontsize = 20)
plt.xticks(fontsize = 13)
plt.grid(False)
plt.show()


# ### Plotting City wise Mean Profit Analysis

# In[179]:


df_city= df.groupby(['City'])[['Sales', 'Discount', 'Profit']].mean()
df_city = df_city.sort_values('Profit')
df_city


# In[202]:


City1 = df_city['Profit'].head(30)

plt.figure(figsize=(10,5))
sns.barplot(x = City1.index, y = City1.values, palette = 'Blues')
plt.xlabel('First 30 Cities',fontsize = 15)
plt.ylabel('Profit',fontsize = 15)
plt.title("Mean Profit earned by first 30 cities",fontsize = 20)
plt.xticks(rotation=90, fontsize = 13)
plt.grid(True)
plt.show()

City2 = df_city['Profit'].tail(30)

plt.figure(figsize=(10,5))
sns.barplot(x = City2.index, y = City2.values, palette = 'Greens')
plt.xlabel('Last 30 Cities',fontsize = 15)
plt.ylabel('Profit',fontsize = 15)
plt.title("Mean Profit earned by last 30 cities",fontsize = 20)
plt.xticks(rotation=90, fontsize = 13)
plt.grid(True)
plt.show()


# ### Plotting State wise Mean Profit Analysis

# In[201]:


State_data= df.groupby([ 'State' ])[['Sales', 'Discount', 'Profit']].mean()
State_data.head(10)


# In[206]:


plt.figure(figsize=(18,10))
sns.barplot(x=State_data.index, y=State_data['Profit'], palette='magma')
plt.title('State wise Mean Profit Analysis', fontsize = 20)
plt.ylabel('Profit per Sate', fontsize = 15)
plt.xlabel('States', fontsize = 15)
plt.xticks(rotation=90, fontsize = 15)
plt.grid(True)
plt.show()


# ### Plotting Pie Charts for Category Plotted against Sales/ Discount/ Profit

# In[211]:


category = df.groupby(['Category'])[['Sales', 'Discount', 'Profit']].mean()
category


# In[219]:


c = ['lightskyblue','pink','gold']
category.plot.pie(subplots=True, figsize=(18, 20), autopct='%1.1f%%', labels = category.index, colors=c)
plt.title('Pie Charts for Category Plotted agaisnt Sales/ Discount/ Profit', fontsize=20)
plt.legend(loc='best')
plt.tight_layout()
plt.show()


# ### Plotting Bar Charts for Sub-Category Plotted against Profit

# In[227]:


p = df.groupby('Sub-Category').min()['Profit'].sort_values()
print(p)
plt.figure(figsize=(8,6))
sns.barplot(x = p.index, y = p, palette='autumn')
plt.title('Sub-Categories with highest loss', fontsize = 20 )
plt.xlabel('Sub-category', fontsize = 15)
plt.ylabel('Profit', fontsize = 15)
plt.xticks(rotation = 60 , fontsize = 15)
plt.yticks(fontsize = 15)
plt.show()


# ### Plotting Pie Charts for Sub-Category Plotted against Sales/ Discount/ Profit

# In[228]:


df_sub_cat = df.groupby(['Sub-Category'])[['Sales', 'Discount', 'Profit']].mean()
df_sub_cat.head(10)


# In[232]:


plt.figure(figsize = (10,10))
plt.pie(df_sub_cat['Sales'], labels = df_sub_cat.index, autopct = '%1.0f%%')
plt.title('Sales Analysis(Sub-Category Wise)', fontsize = 20)
plt.legend(loc='best')
plt.xticks(rotation = 90, fontsize = 10)
plt.show()


# In[233]:


plt.figure(figsize = (10,10))
plt.pie(df_sub_cat['Discount'], labels = df_sub_cat.index, autopct = '%1.1f%%')
plt.title('Discount Analysis(Sub-Category Wise)', fontsize = 20)
plt.legend(loc='best')
plt.xticks(rotation = 90)
plt.show()


# ## Concluding the Analysis:-
# 1. Profit Percentage is more than that of sales but in some cases its vice-versa.
# 2. Sales and Profit are Moderately Correlated.
# 3. Discount and Profit are Negatively Correlated.
# 4. Discount and Profit are Negatively Correlated.
# 5. uantity and sales are also correlated but less than moderate
# 6. Wyoming has the Lowest Number of deal but has the Highest amount of sales(11.8%)
# 7. Lowest amount of sales is present in South Dakota(0.8%)
# 8. Califonia,New York,Texas are the three states with highest deals.
# 9. Ohio has the Lowest Profit and Vermont has the highest profit.
# 10. New York city has the highest city wise dealings.
# 11. West region shows more sales and more profit whereas central region shows least sales and profits. 
# 
# So, one should try to increase sales and profits in central region. Profit percentage can be increased in some cases than sales. The loss in subcategories can be converted into profit percentage.

# In[ ]:




