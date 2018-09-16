## Script to org the data for NFL pick prediction

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# Set data dir
dataDir = 'data/'
   
# Load in data
suffix = '.csv'
df_2003 = pd.read_csv(dataDir+'NFL2003'+suffix)
df_2004 = pd.read_csv(dataDir+'NFL2004'+suffix)
df_2005 = pd.read_csv(dataDir+'NFL2005'+suffix)
df_2006 = pd.read_csv(dataDir+'NFL2006'+suffix)
df_2007 = pd.read_csv(dataDir+'NFL2007'+suffix)
df_2008 = pd.read_csv(dataDir+'NFL2008'+suffix)
df_2009 = pd.read_csv(dataDir+'NFL2009'+suffix)
df_2010 = pd.read_csv(dataDir+'NFL2010'+suffix)
df_2011 = pd.read_csv(dataDir+'NFL2011'+suffix)
df_2012 = pd.read_csv(dataDir+'NFL2012'+suffix)
df_2013 = pd.read_csv(dataDir+'NFL2013'+suffix)
df_2014 = pd.read_csv(dataDir+'NFL2014'+suffix)
df_2015 = pd.read_csv(dataDir+'NFL2015'+suffix)
df_2016 = pd.read_csv(dataDir+'NFL2016'+suffix)
df_2017 = pd.read_csv(dataDir+'NFL2017'+suffix)

# print data
print(df_2003.head())

# Create season to date stats and last season stats (easier per season)
cols = list(df_2003)
# Remoe 'Date' Vis Team' and 'Home Team'
cols = cols[2:18] + cols[19:]

print(cols)


# Concat
frames  = [df_2003,df_2004, df_2005,df_2006,df_2007,df_2008,df_2009,df_2010,df_2011,df_2012,df_2013,df_2014,df_2015,df_2016, df_2017]
df_data = pd.concat(frames)

print(df_data.head())

# replace teams with one hot columns (better than simple integer replacement? TEST)
df_data = pd.get_dummies(df_data, columns=[' Vis Team', 'Home Team'])
print(df_data.head())

# use score prediction as output or winvloss? -> start with win so percentage value can be supplied then try scores


# to parse dates -> d = datetime.datetime.strptime('ISO', '%Y-%m-%d')




