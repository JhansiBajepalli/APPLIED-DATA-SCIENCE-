# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:24:59 2023

@author: 
"""

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv(r'C:\Users\mouli\Downloads\Air_Travelled_Passengers.csv')
data = data.drop(columns=['Series Name', 'Series Code',
                 'Country Code', '2021 [YR2021]'])
data = data.dropna()
data = data.head()
data = data.rename(columns={'Country Name': 'Country'})
print(data)

x = data['Country']

y = data['2014 [YR2014]']

# bar graph of year 2014
plt.figure(figsize=(8, 5))
plt.bar(x, y, label='ATP')
plt.xlabel('Country')
plt.ylabel('ATP')
plt.title('Bar graph of Air transported passengers in year 2014')
plt.legend()
plt.show()
# pie chart of year 2014
plt.figure(figsize=(8, 5))
plt.pie(data['2014 [YR2014]'], labels=data['Country'])
plt.xlabel('Country')
plt.ylabel('ATP')
plt.title('pie chart of Air transported passengers in year 2014')
plt.legend()
plt.show()
# pie chart of year 2020
plt.figure(figsize=(8, 5))
plt.pie(data['2020 [YR2020]'], labels=data['Country'])
plt.xlabel('Country')
plt.ylabel('ATP')
plt.title('pie chart of Air transported passengers in year 2020')
plt.legend()
plt.show()
# line plot
year = ['2014', '2015', '2016', '2017', '2018', '2019', '2020']
plt.figure(figsize=(8, 5))
plt.plot(year, data.iloc[0, 3:10], label='AFG')
plt.plot(year, data.iloc[1, 3:10], label='BAN')
plt.plot(year, data.iloc[2, 3:10], label='BHU')
plt.plot(year, data.iloc[3, 3:10], label='IND')
plt.plot(year, data.iloc[4, 3:10], label='MAL')
plt.xlabel('Year')
plt.ylabel('ATP')
plt.title('line plot of Air transported passengers from 2014 to 2020')
plt.legend()
plt.show()
