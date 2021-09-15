import os
import numpy as np
import pandas as pd
data=pd.read_csv("C:/Users/Dell/OneDrive/Desktop/spotify_dataset.csv")
print(data.Index)
data=pd.read_csv("C:/Users/Dell/OneDrive/Desktop/spotify_dataset.csv", index_col=0)
data.head()
data.shape
data.info()
data.isnull()
data.isnull().sum()    # We don't have any null values
data.index
data.columns
data.size        # 156x22=34232
data.memory_usage()
data.ndim
data.head(7)
data.tail(3)
data.at[12,'Song Name']  # when we are sure aboout column name
data.at[11,'Song Name']
data.iat[0,3]            #When we are sure about row and column index
data.iat[4,3]
data.iat[0,2]
data.loc[0:15,'Song Name']          #To access a group of rows and columns
data.loc[0:10,['Song Name','Artist']]
data.dtypes
#data.get_dtype_counts()
data.select_dtypes(include= [object], exclude=None)
#numpy.unique(Array) tells the unique elements of a column
print(np.unique(data['Chord']))
# To consider '??' '???',etc as  data=pd.read_csv("C:/Users/Dell/OneDrive/Desktop/spotify_dataset.csv", index_col=0,na_values=['?','??'])
data['Number of Times Charted']=data['Number of Times Charted'].astype('object')
data.info() # Data type changed
print(max(data['Duration (ms)'])/60000)










