#for data cleaning, manipulation, and visualization
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
#for iterating through the files in directory
import os
#for printing in a more human-friendly format
import pprint
#for calculating time needed for cleaning
import time
#for storing final dictionary
import json

with open('total_stock_data.json') as json_file:
    total_stock_data = json.load(json_file)
print('loaded')
rk = open(r'data\Stocks in the Russell 1000 Index.csv','r')
reader = csv.reader(rk)
reducedStockData = {}
reducedSymbols = []
i=0
for row in reader:
    if i==0:
        i+=1
        continue
    reducedSymbols.append(row[0])
# print(reducedSymbols)
# reducedStockData = total_stock_data[reducedSymbols]
for (key,value) in total_stock_data.items():
    if key in reducedSymbols:
        reducedStockData[key] = value
with open("reduced_stock_data.json", 'w') as file:
    json.dump(reducedStockData, file)
rk.close()
#hello
