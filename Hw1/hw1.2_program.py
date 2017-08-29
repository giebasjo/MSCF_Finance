"""
MSCF Finance:
    Homework 1

Group:

    Justin Skillman
    Andrew Previc
    Kyle Beyer
    Jordan Giebas

Date:

    28 August 2017
"""

# Used for plotting
#import matplotlib.pyplot as plt
#from itertools import accumulate ## Use this to get the sum of elements in an iterable
from datetime import datetime
import numpy as np
from math import sqrt

def SharpeRatio( asset_expReturn, asset_var, market_r_r ):

    return (asset_expReturn - market_rates)/math.sqrt(asset_var)

def ExpRet_Var_and_Corr( l, bigl ):

    curr_exp_return = 12*np.mean(l) + 0.01
    variance = np.var(l)

    corr_list = list()
    for elm in bigl:

        corr_list.append( round(np.corrcoef(l, elm, ddof=0)[0][1], 3) )

    return [curr_exp_return, variance, corr_list]

## Define containers for needed quantitites
rf_rates = list()
market_rates = list()
aero_rates = list()
guns_rates = list()
steel_rates = list()
ships_rates = list()
beer_rates = list()
toys_rates = list()
fin_rates = list()
rtail_rates = list()

with open('Industry8_data.csv', 'r') as dataFile:

    header_line = dataFile.readline()
    for line in dataFile:

        L = line.strip().split(",")

        market_rates.append(float(L[13]))
        aero_rates.append(float(L[14]))
        guns_rates.append(float(L[15]))
        steel_rates.append(float(L[16]))
        ships_rates.append(float(L[17]))
        beer_rates.append(float(L[18]))
        toys_rates.append(float(L[19]))
        fin_rates.append(float(L[20]))
        rtail_rates.append(float(L[21]))

## Define assetList, list of lists
## contain the lists of each of the assets
assetList = list()
assetList.append(market_rates)
assetList.append(aero_rates)
assetList.append(guns_rates)
assetList.append(steel_rates)
assetList.append(ships_rates)
assetList.append(beer_rates)
assetList.append(toys_rates)
assetList.append(fin_rates)
assetList.append(rtail_rates)

bigList = list()

## Market
market_cer, market_var, market_corr = ExpRet_Var_and_Corr(market_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(market_rates, assetList))

## Aero
aero_cer, aero_var, aero_corr = ExpRet_Var_and_Corr(aero_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(aero_rates, assetList))

## Guns
guns_cer, guns_var, guns_corr = ExpRet_Var_and_Corr(guns_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(guns_rates, assetList))

## Steel
steel_cer, steel_var, steel_corr = ExpRet_Var_and_Corr(steel_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(steel_rates, assetList))

## Ships
ships_cer, ships_var, ships_corr = ExpRet_Var_and_Corr(ships_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(ships_rates, assetList))

## Beer
beer_cer, beer_var, beer_corr = ExpRet_Var_and_Corr(beer_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(beer_rates, assetList))

## Toys
toys_cer, toys_var, toys_corr = ExpRet_Var_and_Corr(toys_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(toys_rates, assetList))

## Fin
fin_cer, fin_var, fin_corr = ExpRet_Var_and_Corr(fin_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(fin_rates, assetList))

## Rtail
rtail_cer, rtail_var, rtail_corr = ExpRet_Var_and_Corr(rtail_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(rtail_rates, assetList))




cov_matrix = list()
cov_matrix.append(market_corr)
cov_matrix.append(aero_corr)
cov_matrix.append(guns_corr)
cov_matrix.append(steel_corr)
cov_matrix.append(ships_corr)
cov_matrix.append(beer_corr)
cov_matrix.append(toys_corr)
cov_matrix.append(fin_corr)
cov_matrix.append(rtail_corr)

## print covariance matrix (even though this is truly unneeded)
print('\n'.join([' '.join(['{:4}'.format(item) for item in row])
      for row in cov_matrix]))





