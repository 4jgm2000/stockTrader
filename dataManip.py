import numpy as numpy
import pandas as pd
import json
import random
from sklearn.mixture import GaussianMixture
# turn dictionary into panda dataframe, import and use as array for GMM
# inputArray = np.array([1, 2])


#Data is in the form of a numpy array, I belive it is (stock(ticker), data up till 2019)
#indList is useful to find the specific ticker for the index of the stock
#Certain stocks, such as 616 out of the 694 list was extreme broken
#This may not work for other implementations but worked for gmm. Consider converting the np array to pandas dataframe if necessary

with open('reduced_dimension_stock_data.json') as json_file:
    stocks = json.load(json_file)

indList = []
#print(len(stocks)) 
for (key,value) in stocks.items():
    try:
        # print(value['Date'])
        cur = value['Date']
        indList.append(cur.index('2019-01-02', -900, -1))
        # cur = pd.DataFrame.from_dict(value['Date'])
        del value['Date']
    except Exception:
        indList.append(0)
        del value['Date']


inputArray = pd.DataFrame.from_dict(stocks, orient='index')
#find longest sub-array
longest = 0
i=0
for (key, value) in stocks.items():
    if (len(inputArray.loc[key].at['Open']) > longest):
        longest = len(inputArray.loc[key].at['Open'])
    i+=1
#print("longest:")
#print(longest)
#in this dataset, longest is 14665
longest -= 365
i=0
err = 0
tick = {}
apple = None
for (key,value) in stocks.items():
    cur = inputArray.loc[key].at['Open']
    inputArray.at[key,'Open'] = cur[0:indList[i]]
    #duplicate first element to make array lengths match
    if key == 'AAPL':apple = i
    # print(inputArray.at[key,'Open'][0])
    try:
        firstEle = inputArray.at[key,'Open'][0]
        # print(firstEle, key)
        
        # print(firstEle != '0.0', firstEle)
        if (firstEle != '0.0'):
            cre = numpy.array([firstEle for j in range(longest - len(inputArray.at[key, 'Open']))])
            # print(cre)
            inputArray.at[key,'Open'] = numpy.append(cre,inputArray.at[key,'Open'])
            i+=1
            tick[i-err] = key
            # print(len(inputArray.at[key,'Open']) == longest)
        else:
            i+=1
            err+=1
            # print(i)
            # inputArray.drop(i,axis=0)
            inputArray = inputArray.drop(key)
            # i+=1
    except Exception:
        i+=1
        err+=1
        # print(i)
        # print('here')
        inputArray = inputArray.drop(key)
        # i+=1
print(len(inputArray))
arr = pd.DataFrame.to_numpy(inputArray)
print(numpy.shape(arr))
print('sjhdgadjhlfgbadsv',arr[0][0]) 
newArr = numpy.zeros((694,longest))
print(numpy.shape(arr), numpy.shape(arr[0]), numpy.shape(newArr))
for i in range(694):
    try:
        if(i == 616): continue
        newArr[i,:] = arr[i][0]
    except Exception:
        print(i)inputArray = pd.DataFrame.from_dict(stocks, orient='index')
#find longest sub-array
longest = 0
i=0
for (key, value) in stocks.items():
    if (len(inputArray.loc[key].at['Open']) > longest):
        longest = len(inputArray.loc[key].at['Open'])
    i+=1
#print("longest:")
#print(longest)
#in this dataset, longest is 14665
longest -= 365
i=0
err = 0
tick = {}
apple = None
for (key,value) in stocks.items():
    cur = inputArray.loc[key].at['Open']
    inputArray.at[key,'Open'] = cur[0:indList[i]]
    #duplicate first element to make array lengths match
    if key == 'AAPL':apple = i
    # print(inputArray.at[key,'Open'][0])
    try:
        firstEle = inputArray.at[key,'Open'][0]
        # print(firstEle, key)
        
        # print(firstEle != '0.0', firstEle)
        if (firstEle != '0.0'):
            cre = numpy.array([firstEle for j in range(longest - len(inputArray.at[key, 'Open']))])
            # print(cre)
            inputArray.at[key,'Open'] = numpy.append(cre,inputArray.at[key,'Open'])
            i+=1
            tick[i-err] = key
            # print(len(inputArray.at[key,'Open']) == longest)
        else:
            i+=1
            err+=1
            # print(i)
            # inputArray.drop(i,axis=0)
            inputArray = inputArray.drop(key)
            # i+=1
    except Exception:
        i+=1
        err+=1
        # print(i)
        # print('here')
        inputArray = inputArray.drop(key)
        # i+=1
print(len(inputArray))
arr = pd.DataFrame.to_numpy(inputArray)
print(numpy.shape(arr))
print('sjhdgadjhlfgbadsv',arr[0][0]) 
newArr = numpy.zeros((694,longest))
print(numpy.shape(arr), numpy.shape(arr[0]), numpy.shape(newArr))
for i in range(694):
    try:
        if(i == 616): continue
        newArr[i,:] = arr[i][0]
    except Exception:
        print(i)

