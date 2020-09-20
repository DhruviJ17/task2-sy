import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt

df = pd.read_json('https://raw.githubusercontent.com/theand9/data-viz-challenge/master/data.json')
data = json_normalize(df['data'])

# number of users as per event type
d = data.event_name.drop_duplicates()
events = d.tolist()
users = data['event_name'].value_counts()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
project_g = events
user_g = [x for x in users]
ax.bar(project_g , user_g)
plt.show


# number of users as per gender
d = data.gender.drop_duplicates()
gender = d.tolist()
users1 = data['gender'].value_counts()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
gender_g = gender
user_g = [x for x in users1]
ax.bar(gender_g , user_g)
plt.show

# number of users as per age
d = data.age.drop_duplicates()
age = d.tolist()
users2 = data['age'].value_counts()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
age_g = age
user_g = [x for x in users2]
ax.bar(age_g , user_g)
plt.show

# pie diagram for event types and users
df = pd.read_json('https://raw.githubusercontent.com/theand9/data-viz-challenge/master/data.json')
data = json_normalize(df['data'])
d = data.event_name.drop_duplicates()
events = d.tolist()
labels = events
users = data['event_name'].value_counts()
user_g = [x for x in users]
plt.pie(user_g,labels=labels,autopct='%1.1f%%')
plt.show()

# pie diagram for gender types and users
d = data.gender.drop_duplicates()
events = d.tolist()
labels = events
users = data['gender'].value_counts()
user_g = [x for x in users]
plt.pie(user_g,labels=labels,autopct='%1.1f%%')
plt.show()

# similarly pie charts for others