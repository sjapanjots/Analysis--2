
"""
# Analysis report 2
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

path = '/content/drive/MyDrive/data analysis 2/8. Netflix Dataset.csv'
data = pd.read_csv(path)
data.head()

# 1. head()

data.head()

# tail 
data.tail()
# this function helps to show the last records of the dataset

#shape
data.shape
#  to show the no. rows and columns

#size 
data.size
# to show the total number of (elements) in the dataset

#columns 
data.columns 
#to show the each column name

#dtypes 
data.dtypes
# to show the data type of the each column

#info 
data.info()
# to show indexes , columns , data-types of each columns , memory at once



"""Task 1. Is there any duplicate records in this dataset? if yes then remove the duplicate records

Duplicate
"""

data.head()

data.shape

data.duplicated()      # use of duplicated function here

data[data.duplicated()]     # now by doing this it only shows the duplicated rows of the dataset

data.drop_duplicates( inplace = True )     # with the hepl of this command duplicated row permanently deleted

data[data.duplicated()]     # now check wheater it shows any duplicated records or not

data.shape        # as we seen that now it's 7787 as before it was 7789

"""Task 2. Is there any null value present in any column ? show the heat-map

isnull()
"""

data.isnull()    # to show null values presented in dataset

data.isnull().sum()      # now with sum () function it counts that how many null values as presented in dataset

"""Seaborn library (heat-map)"""

import seaborn as sns                                 # To import seaborn library

sns.heatmap(data.isnull())                   #Using heat-map to show the null values count

"""### 1. For 'House of cards' , What is the show Id and Who is the Director of this show?

isin()
"""

data['Title'].isin(['House of Cards'])     #to show all records of particular item in any column

data[data['Title'].isin(['House of Cards'])]

"""or we can use a different method

str.contains()
"""

data['Title'].str.contains('House of Cards')    # To show all records of particluar string in any column

data[data['Title'].str.contains('House of Cards')] # to show all records of a particluar string in any column

"""Q2. In which year highest number of the TV shows & movies were released ? show with bar graph

dtypes
"""

data.dtypes

"""To_datetime"""

data['Date_N'] = pd.to_datetime(data['Release_Date'])

data.head()

data.dtypes

"""dt.year.value_counts()"""

data['Date_N'].dt.year.value_counts()  # it count the occurance of all individual year in date column.

"""Bar Graph"""

data['Date_N'].dt.year.value_counts().plot(kind='bar')

"""### Q3 How many Movies & TV shows are in the dataset? Show with Bar Graph

Groupby()
"""

data.groupby('Category').Category.count()                 # To group all unique items of a column and their count

"""## Q4 show all the movies that were released in year 2000."""

# data.head()
data.head(2)

# data['Year'] = data['Date_N'].dt.year    # to create new year column ; it will consider only year 
data['Year'] = data['Date_N'].dt.year

data.head(2)

"""Filtering

"""

#data[ (data['Category']=='Movies') & (data['Year']==2020)]
data[ (data['Category']=='Movies') & (data['Year']==2000)]

data[ (data['Category'] == 'Movies') & (data['Year']==2020) ]

"""Q5 Show only the Titles of all TV shows that were released in India only.

Filtering
"""

data.head(2)

# data [( data['Category'] == 'TV Shows) & (data['countary'] == 'India')] ['Title']
data [(data['Category'] == 'TV show') & (data['Country'] == 'India')]

data [(data['Category'] == 'TV show') & (data['Country'] == 'India')] ['Title']

"""Q6 Show the top 10 directors , who gave the highest number of tv shows & Movies to netflix ?"""

#value_counts()
data['Director'].value_counts().head(10)                                 # data ['Directors'].value_counts().head(10)

"""Q7 show all the records , where "Category is movies and type is comedies " or " country i sunited kindom".

## FIltering ( And , Or operators )
"""

# data[(data['category']=='movies') & (data['Type] == 'comedies')]
 data[(data['Category']=='Movie') & (data['Type']=='Comedies') ]

data[(data['Category']=='Movie') & (data['Type']=='Comedies') | (data['Country']== 'United Kindom') ]             # data[(data ['Category']=='Movies') & (data['Type'] == 'Comedies') | (data['Counrty'] == 'United Kindom') ]

"""Q8 In how many movies/shows , Tom Cruise was cast?"""

# data[data['Cast']=='Tom Cruise']
data[data['Cast'] == 'Tom Cruise']

"""Creating a dataframe 

"""

#data_new = data.dropna()           # it drops the rows that contains all or any missing values.
 data_new = data.dropna()

# data_new.head(2)
data_new.head(2)

# data_new[data_new['Cast'].str.contains('Tom Cruise')]
 data_new[data_new['Cast'].str.contains('Tom Cruise')]

"""Q9 What are the diffrenet Rating defined by Netflix ?

nunique()
"""

# data.Rating.nunique()
data['Rating'].nunique()

"""Unique()



"""

data['Rating'].unique()

"""Q9.1. How many Movies got the 'TV-14', rating in Canada?"""

# data[(data['Category']== 'Movie') & (data['Rating'] == 'TV-14')].shape
data[(data['Category']=='Movie' ) & (data['Rating']=='TV-14')].shape

data[(data['Category']=='Movie' ) & (data['Rating']=='TV-14') & (data['Country'] == 'Canada')].shape

"""Q9.2 How many tv shows got the 'R' rating , after year 2018?"""

#data[(data['Category'] == 'TV show') & (data['Rating'] == 'R')]
data[(data['Category'] == 'TV show') & (data['Rating'] == 'R')]

data[(data['Category'] == 'TV show') & (data['Rating'] == 'R') & (data['Year'] > 2018)]

"""Q10 What is the maximum duration of movie/show on netflix?"""

# data.head(2)
data.head(2)

data.Duration.unique()

#data.Duration.dtypes
data.Duration.dtypes

"""str.split()"""

data.head(2)

#data[['Minutes' , 'Unit']] == data=['Duration'].str.split(' ', expand = True)
data[['Minutes' , 'Unit']] = data['Duration'].str.split(' ', expand = True)

# data.head(2)
data.head(2)



"""max()"""

# data.Minutes.max()
data['Minutes'].max()

data['Minutes'].min()

data['Minutes'].mean()

data.dtypes

"""Q11. Which individual country has the highest no. of tv shows?"""

#data.head(2)
data.head(2)

# data_tvshow = data[data['category'] == 'TV show']
data_tvshow = data[data['Category'] == 'TV Show']

data_tvshow.head(2)

# data_tvshow.Country.value_couhnts()
data_tvshow.Country.value_counts()

# data_tvshow.country.value_counts().head(1)
data_tvshow.Country.value_counts().head(1)

"""Q12 How can we sort the dataset by year?

"""

# data.head()
data.head(2)

#data.sort_values(by= 'year').head(2)
data.column.sort_values(by = 'Year')

# data.sort_values(by = 'year' , ascending = false).head(2)
data.sort_values(by = 'year' , ascending = False)

"""  Q13 Find all the Instances where:
  category is 'movie ' and type is 'dramas'
  or
  category is 'tv show ' & type is kinds 
"""

data[ (data['Category']=='Movie') & (data['Type'] == 'Dramas') ]

data[ (data['Category']=='Movie') & (data['Type'] == 'Dramas')]

data [ (data['Category']=='Movie') & (data['Type'] == 'Dramas') | (data['Category']=='TV Show') & (data['Type']== 'kids TV') ]

