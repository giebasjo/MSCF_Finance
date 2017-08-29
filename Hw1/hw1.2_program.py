"""
MSCF Finance:
    Homework 1

Group:

    Jordan Giebas
    Justin Skillman
    Andrew Previc
    Kyle Beye

Date:

    28 August 2017
"""

# Used for plotting
#import matplotlib.pyplot as plt
#from itertools import accumulate ## Use this to get the sum of elements in an iterable
from datetime import datetime
import numpy as np

def curr_exp_return( l ):

    return 12*np.mean(l) + 0.01


def Var_and_Corr( l, bigl ):

    variance = np.var(l)

    corr_list = list()
    for elm in bigl:

        corr_list.append( np.corrcoef(l, elm, ddof=0)[0][1] )

    return [variance, corr_list]

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


## Market
market_var, market_corr = Var_and_Corr(market_rates, assetList)

## Aero
aero_var, aero_corr = Var_and_Corr(aero_rates, assetList)

## Guns
guns_var, guns_corr = Var_and_Corr(guns_rates, assetList)

## Steel
steel_var, steel_corr = Var_and_Corr(steel_rates, assetList)

## Ships
ships_var, ships_corr = Var_and_Corr(ships_rates, assetList)

## Beer
beer_var, beer_corr = Var_and_Corr(beer_rates, assetList)

## Toys
toys_var, toys_corr = Var_and_Corr(toys_rates, assetList)

## Fin
fin_var, fin_corr = Var_and_Corr(fin_rates, assetList)

## Rtail
rtail_var, rtail_corr = Var_and_Corr(rtail_rates, assetList)

print(aero_corr)
print(rtail_corr)














"""
Going to get the current expected return
for each of the different assets.
cer == curent expected return


market_cer = curr_exp_return(market_rates)
aero_cer = curr_exp_return(aero_rates)
guns_cer = curr_exp_return(guns_rates)
steel_cer = curr_exp_return(steel_rates)
ship_cer = curr_exp_return(ships_rates)
beer_cer = curr_exp_return(beer_rates)
toy_cer = curr_exp_return(toys_rates)
fin_cer = curr_exp_return(fin_rates)
rtail_cer = curr_exp_return(rtail_rates)

print(np.corrcoef(market_rates, aero_rates, ddof=0)[0][1])
print(np.corrcoef(market_rates, guns_rates, ddof=0)[0][1])


"""
















