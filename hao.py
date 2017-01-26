# -*- coding: utf-8 -*-

"""

Created on Mon Nov 24 12:29:15 2014



@author: Sonya

"""

import numpy as np

import scipy as sp

import pandas as pd

import matplotlib

import sklearn

import matplotlib.pyplot as plt

import urllib2

import json

import time

from sklearn.svm import SVR

from sklearn.cross_validation import train_test_split

from datetime import date

from datetime import timedelta

# dd5d40d33cfeef62

obsdata = pd.DataFrame()  # empty data frame

obsdatafull = pd.DataFrame()

currentdate = date(2009, 8, 5)  # starting date

# f = urllib2.urlopen('http://api.wunderground.com/api/c72bd93c933fdefa/history_20080101/q/France/Paris.json')

for i in range(86, 494):

    apiurl = 'http://api.wunderground.com/api/c57a079b633c10ab/history_' + \
             str(currentdate.year) + currentdate.strftime('%m') + currentdate.strftime('%d') + '/q/France/Paris.json'

    print
    str(i) + ". " + apiurl

    f = urllib2.urlopen(apiurl)

    json_string = f.read()

    parsed_json = json.loads(json_string)

    histdata = parsed_json['history']

    obsdataNew = pd.DataFrame(histdata['observations'])

    obsdatafull = obsdatafull.append(obsdataNew)

    obsdatacut = pd.DataFrame()

    # newindexsize=obsdata.shape[0]

    # newindex=np.arange(0,newindexsize)

    obsdatacut['datetime'] = obsdataNew.date

    obsdates = pd.DataFrame.from_records(obsdatacut['datetime'])

    obsdatacut['year'] = obsdates['year'].astype(int)

    obsdatacut['month'] = obsdates['mon'].astype(int)

    obsdatacut['day'] = obsdates['mday'].astype(int)

    obsdatacut['hour'] = obsdates['hour'].astype(int)

    obsdatacut['minutes'] = obsdates['min'].astype(int)

    obsdatacut['temp'] = obsdataNew.tempm  # .astype(float)

    obsdatacut['hum'] = obsdataNew.hum  # .astype(int)

    obsdatacut['rain'] = obsdataNew.rain  # .astype(float)

    obsdata = obsdata.append(obsdatacut)

    deltadate = timedelta(days=1)

    currentdate = currentdate + deltadate

    if np.mod(i, 50) == 0:
        obsdata.to_csv('tempsaveobsdata_' + str(i) + '.csv')

        obsdatafull.to_csv('tempsaveobsdatafull_' + str(i) + '.csv')

    time.sleep(7)  # wait for 6 seconds

print
'Done!'

obsdata.drocp('datetime', axis=1, inplace=True)

# drop all values with nonzero minutes

obsdata = obsdata[obsdata.minutes == 0]

obsdata.drop('minutes', axis=1, inplace=True)

# obsdata_multiindex=pd.pivot_table(obsdata,index=['year','month','day','hour'])



obsdata.to_csv('Tinu_obsdata.csv')

obsdatafull.to_csv('Tinu_obsdatafull.csv')

