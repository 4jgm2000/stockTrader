import numpy as numpy
import pandas as pd
import json

from sklearn.mixture import GaussianMixture
# turn dictionary into panda dataframe, import and use as array for GMM
# inputArray = np.array([1, 2])
with open('reduced_dimension_stock_data.json') as json_file:
    stocks = json.load(json_file)

indList = []
#print(len(stocks))
for (key,value) in stocks.items():
    try:
        # print(value['Date'])
        cur = value['Date']
        indList.append(cur.index('2019-01-02', -700, -1))
        # cur = pd.DataFrame.from_dict(value['Date'])
        del value['Date']
    except Exception:
        indList.append(0)
        del value['Date']
#print(indList[0:100])



inputArray = pd.DataFrame.from_dict(stocks, orient='index')
#find longest sub-array
longest = 0
for (key, value) in stocks.items():
    if (len(inputArray.loc[key].at['Open']) > longest):
        longest = len(inputArray.loc[key].at['Open'])
#print("longest:")
#print(longest)
#in this dataset, longest is 14665

i=0
for (key,value) in stocks.items():
    cur = inputArray.loc[key].at['Open']
    inputArray.at[key,'Open'] = cur[0:indList[i]]
    #duplicate first element to make array lengths match
    if (len(inputArray.loc[key].at['Open']) < longest):
        j=0
        while (j < (longest - len(inputArray.loc[key].at['Open']))):
            
            j+=1
    i+=1 
#print(indList[0], len(inputArray.loc['A'].at['Open']))
#print(inputArray.loc['A'].at['Open'])
gm = GaussianMixture(n_components=3, random_state=0).fit_predict(inputArray)
