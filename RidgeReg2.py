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

gain_dict = {} #dictionary of values mapped to stock tickers
gain_vals = [] #list of 2020 values relative to 2019
est_val_list = [] #list of estimated stock prices for 2020
sq_err = 0 # holds cumulative squared error of stock prices
rel_gain_sq_err = 0 # hold cumulative squared error of relative gain
#iterate through each stock in stock dictionary  and perform polynomial regression on each stock individually from the start of 2000 to start of 2019
for stock in stocks:
    #print(stocks[stock])
    i=0
    if stock == 'NET':
        continue
    if stock == 'TT':
        continue
    if stock == 'IAA':
        continue
    for i in range(len(stocks[stock]['Date'])):
        if stocks[stock]['Date'][i] >= '2000-01-02':
            #print(i)
            #print(stocks[stock]['Date'][i])
            break
    if (len(stocks[stock]['Open'][i:-315]) > 100 ): # only use stocks that have atleast 100 values to perform regression on
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
        act_val = float(stocks[stock]['Open'][-63]) # actual value on 2020-01-02
        #print(stock)
        #print("2019 value", open_list[-1])
        #print("2020 Prediction",predict(len(open_list)+251)) #predicted value after 1 year
        #print(model) - set of coefficients
        #print(stock)
        est_gain = est_val / open_list[-1]
        #print(est_gain)
        act_gain = act_val / open_list[-1]
        #print(act_gain)
        sq_err = sq_err + (act_val - est_val)**2
        rel_gain_sq_err = rel_gain_sq_err + (act_gain - est_gain)**2
        #print(rel_gain_sq_err)
        #print(stock, sq_err)
        gain_dict.update({est_gain: stock}) #record relative expected value on Jan 2, 2020 compared to Jan 2, 2019
        gain_vals.append(est_gain)
        
print("Stocks tested",len(gain_vals))
#print("(y_a -y_p)^2",sq_err)
sq_err = np.sqrt(sq_err / len(gain_vals)) # stock price calculate RSME
print("Stock Price RMSE: ", sq_err)
rel_gain_sq_err = np.sqrt(rel_gain_sq_err / len(gain_vals)) # calculate relative gain RSME
print("Relative Gain RMSE", rel_gain_sq_err)
gain_vals.sort(reverse=True) #sort the list from high to low
#print(gain_vals)
#print("Expected gain from top 20 stocks: ", gain_vals[:20])
#print(gain_dict)
stock_picks = []
for i in gain_vals[:20] : # get 10 highest gain stocks
    #print(i)
    #print(gain_dict[i])
    stock_picks.append(gain_dict[i])
print("Best stocks: ", stock_picks) #return 20 highest value stock picks
#print("All Stocks: ", gain_dict)
#print(gain_vals)







