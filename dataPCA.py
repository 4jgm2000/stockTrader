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
from sklearn.decomposition import PCA

with open('reduced_stock_data.json') as json_file:
    stocks = json.load(json_file)

num = 0
var = np.zeros(5)
pca = PCA(n_components = 'mle', svd_solver='full')
for (key,value) in stocks.items():
    try:
        stockNoDate = value.copy()
        del stockNoDate['Date']
        curStock = pd.DataFrame.from_dict(stockNoDate)

        pca.fit(curStock)
        num += 1
        var += pca.explained_variance_ratio_
    except:
        print(key)
        
var /= num
print(var)

# #
#   ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'] with date taken out of the pca algorithm

# # [9.99995279e-01 4.71666551e-06 2.85886929e-09 1.04067581e-09
# #  1.14000655e-10]


# Open works to collect all of the data necessary, and the other data adds uneccesary complexity to the algorithm quite drastically.
# # 
    

#     Worth noting that these datasets could not be ran due to incomplete data  ~75 of the 1000
# ADP
# AIG
# ALB
# AMAT
# AME
# AON
# AOS
# AVT
# AXP
# BAC
# BK
# BLL
# BMY
# BPOP
# CAG
# CAH
# CAT
# CBSH
# CLF
# CMA
# CMI
# CUZ
# DVN
# ECL
# EL
# EMN
# EXPD
# FHN
# GIS
# GL
# GLW
# GPS
# HAL
# HBAN
# HES
# HOG
# HUN
# JBHT
# JCI
# KDP
# KMI
# KO
# LB
# LMT
# LNC
# LNT
# LUV
# MCY
# MDLZ
# MDU
# MO
# MOS
# MS
# MSI
# NEM
# NI
# NKE
# NLOK
# NNN
# NOC
# NVDA
# ODFL
# OHI
# PB
# PEAK
# PEN
# PGR
# PH
# PSA
# R
# RCL
# RHI
# ROST
# RYN
# SEB
# SF
# SYY
# TDS
# TROW
# TXN
# TXT
# VST
# WHR
# WMB
# WTRG
# XRAY
# XRX

