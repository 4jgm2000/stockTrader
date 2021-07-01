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


with open('reduced_stock_data.json') as json_file:
    stocks = json.load(json_file)
for (key,value) in stocks.items():
    del value['Close']
    del value['High']
    del value['Low']
    del value['Adj Close']
    del value['Volume']

with open("reduced_dimension_stock_data.json", 'w') as file:
    json.dump(stocks, file)