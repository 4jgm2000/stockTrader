import numpy as numpy
import pandas as pd
import json

from sklearn.mixture import GaussianMixture
# turn dictionary into panda dataframe, import and use as array for GMM
# inputArray = np.array([1, 2])
with open('reduced_dimension_stock_data.json') as json_file:
    stocks = json.load(json_file)

indList = []
print(len(stocks))
for (key,value) in stocks.items():
    try:
        # print(value['Date'])
        cur = value['Date']
        indList.append(cur.index('2019-01-02', -700, -1))
        # cur = pd.DataFrame.from_dict(value['Date'])

    except Exception:
        indList.append(0)
print(indList[0:100])
# gm = GaussianMixture(n_components=3, random_state=0).fit_predict(inputArray)

