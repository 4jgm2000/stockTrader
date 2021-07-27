import numpy as np
import pandas as pd
import json
from sklearn import linear_model
from sklearn.metrics import r2_score

#read data from json
stocks = pd.read_json('reduced_dimension_stock_data.json')

# test regression on one value
""" a = stocks['A']['Date']

for i in range(len(a)):
    if a[i] >= '2000-01-02':
        print(i)
        break
x = np.arange(len(stocks['A']['Date'][i:-315])) # list 
open_list = np.array(stocks['A']['Open'][i:-315])
open_list = open_list.astype(np.float)
print(len(stocks['A']['Date'][i:-315]))
print(x)
print(len(stocks['A']['Open'][i:-315]))
print(range(len(stocks['A']['Open'][i:-315])))
print(type(x))
print(type(open_list))
print(open_list)

model = np.polyfit(x=x, y=open_list, deg=3) #perform regression
predict = np.poly1d(model) #make the equation from the model
est_val = predict(x[-1] + 251) # estimated value on 2020-01-02 - 1 fiscal year later
print(predict(4779+251)) #predicted value after 1 year
print(est_val)
print(model)


# test metrics
print("r2 score: ", r2_score(open_list, predict(x))) """

#list of date ranges - test dates
""" j = 0
for (key, value) in stocks.items():
    print(j) #stock index by alphabetical
    print(key) #stock tickers
    if len(value['Date']) > 315:
        if (value['Date'][-315] == '2019-01-02'):
            print(value['Date'][i])
            print(value['Date'][-315])
    #print(value['Open'])
    j+=1 """

gain_dict = {}
gain_vals = []
#iterate through each stock in stock dictionary  and perform polynomial regression on each stock individually from the start of 2000 to start of 2019
for stock in stocks:
    #print(stocks[stock])
    i=0
    for i in range(len(stocks[stock]['Date'])):
        if stocks[stock]['Date'][i] >= '2000-01-02':
            #print(i)
            #print(stocks[stock]['Date'][i])
            break
    if (len(stocks[stock]['Open'][i:-315]) > 100 ):
        x = np.arange(len(stocks[stock]['Date'][i:-315])) # list 
        open_list = np.array(stocks[stock]['Open'][i:-315])
        #print(len(open_list))
        try:
           open_list = open_list.astype(np.float)
        except Exception:
            #print("Bad data in array")
            continue
        #print(x)
        model = np.polyfit(x=x, y=open_list, deg=2) #perform regression
        predict = np.poly1d(model) #make the equation from the model
        est_val = predict(x[-1] + 251) # estimated value on 2020-01-02 - 1 fiscal year later
        #print(stock)
        #print("2019 value", open_list[-1])
        #print("2020 Prediction",predict(len(open_list)+251)) #predicted value after 1 year
        #print(model) - set of coefficients
        est_gain = est_val / open_list[-1]
        gain_dict.update({est_gain: stock}) #record relative expected value on Jan 2, 2020 compared to Jan 2, 2019
        gain_vals.append(est_gain)
gain_vals.sort(reverse=True) #sort the list from high to low
#print(gain_vals)
print("Expected gain from top 20 stocks: ", gain_vals[:20])
#print(gain_dict)
stock_picks = []
for i in gain_vals[:20] : # get 10 highest gain stocks
    #print(i)
    #print(gain_dict[i])
    stock_picks.append(gain_dict[i])
print("Best stocks: ", stock_picks)






#return 20 highest values
