import pandas as pd
import numpy as np
from pandas.io.json import json_normalize


df = pd.read_json('https://raw.githubusercontent.com/theand9/data-viz-challenge/master/data.json')
data = json_normalize(df['data'])
data.drop(['location.latitude','location.longitude','location.state','location.zip_code','device'],1, inplace=True)
#data.head()
data1 = data[data['category'].isin(['Sports', 'Environment']) & (data['event_name'] == 'Fund Project')]
data1.head(1000)
sort = data1.sort_values(['gender','age','marital_status','category','location.city'])
sort.head(40)
sort.isnull()
duplicateRows = sort[sort.duplicated(['category', 'session_id','location.city','gender','age','amount'])]
#duplicateRows = sort[sort.duplicated(keep=False)]  #for all columns
duplicateRows.head()
sort.drop_duplicates(subset =['category', 'session_id','location.city','gender','age','amount'])
sort.max()
top = sort.loc[sort['amount'].idxmax()]
print(top)
sort.nlargest(30,['amount']) #top 30 funding users as per the amount
