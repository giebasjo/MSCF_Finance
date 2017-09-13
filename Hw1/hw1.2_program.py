"""
MSCF Finance:
    Homework 1

Author:

    Jordan Giebas

Date:

    28 August 2017
"""

# Used for plotting
import matplotlib.pyplot as plt
#from itertools import accumulate ## Use this to get the sum of elements in an iterable
from datetime import datetime
import numpy as np
from math import sqrt


def SharpeRatio( asset_expReturn, asset_var, market_r_r ):

    return (asset_expReturn - market_rates)/sqrt(asset_var)

def ExpRet_Var_and_Corr( l, bigl ):

    # Quantities of interest
    curr_exp_return = round(float(12*np.mean(l) + 0.01), 3)
    avg_monthly_variance = np.var(l)
    annual_variance = round(float(12*avg_monthly_variance),3)
    annual_std = sqrt(annual_variance)
    sharpe_ratio = round((curr_exp_return - 0.01)/float(annual_std),3)

    corr_list = list()
    for elm in bigl:

        corr_list.append(round(float(np.corrcoef(l, elm, ddof=0)[0][1]),3))

    return [sharpe_ratio, curr_exp_return, annual_variance, corr_list]

# Define containers for needed quantitites
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

# Define assetList, list of lists
# contain the lists of each of the assets
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


# Question 2: Parts a,b,c
# Get needed quantities

#print("\nSHARPE RATIOS\n")
## Market
market_sr, market_cer, market_var, market_corr = ExpRet_Var_and_Corr(market_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(market_rates, assetList))

#print( "Market: ", market_cer, ",", market_var, ",", market_sr )

## Aero
aero_sr, aero_cer, aero_var, aero_corr = ExpRet_Var_and_Corr(aero_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(aero_rates, assetList))

#print( "\nAero: ", aero_cer, ",", aero_var, ",", aero_sr )


## Guns
guns_sr, guns_cer, guns_var, guns_corr = ExpRet_Var_and_Corr(guns_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(guns_rates, assetList))

#print( "\nGuns: ", guns_cer, ",", guns_var, ",", guns_sr )


## Steel
steel_sr, steel_cer, steel_var, steel_corr = ExpRet_Var_and_Corr(steel_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(steel_rates, assetList))

#print( "\nSteel: ", steel_cer, ",", steel_var, ",", steel_sr )

## Ships
ships_sr, ships_cer, ships_var, ships_corr = ExpRet_Var_and_Corr(ships_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(ships_rates, assetList))

#print( "\nShips: ", ships_cer, ",", ships_var, ",", ships_sr )

## Beer
beer_sr, beer_cer, beer_var, beer_corr = ExpRet_Var_and_Corr(beer_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(beer_rates, assetList))

#print( "\nBeer: ", beer_cer, ",", beer_var, ",", beer_sr )

## Toys
toys_sr, toys_cer, toys_var, toys_corr = ExpRet_Var_and_Corr(toys_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(toys_rates, assetList))

#print( "\nToys: ", toys_cer, ",", toys_var, ",", toys_sr )

## Fin
fin_sr, fin_cer, fin_var, fin_corr = ExpRet_Var_and_Corr(fin_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(fin_rates, assetList))

#print( "\nFin: ", fin_cer, ",", fin_var, ",", fin_sr )

## Rtail
rtail_sr, rtail_cer, rtail_var, rtail_corr = ExpRet_Var_and_Corr(rtail_rates, assetList)
bigList.append(ExpRet_Var_and_Corr(rtail_rates, assetList))

#print( "\nRtail: ", rtail_cer, ",", rtail_var, ",", rtail_sr )


# Question 2: Part d,e
# Build Portfolio frontier for a portfolio
# consisting of beer and finance

beer_fin_cov = float(np.cov(beer_rates, fin_rates)[0][1])
#print(beer_fin_cov)

# Construct list of weights to construct frontier
weights = list()
for i in range(0,1001):

    i = i/1000.0
    temp = [i, 1.0-i]
    weights.append(temp)


# Building of the Correlation Matrix

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

x = np.array(cov_matrix)
m = np.asmatrix(x)
print(m)


"""
mean_returns = list()
risk = list()
sharpe_ratio_to_weights = dict()  # Assuming they will all be unique (ehh....)
for w in weights:

    delta_beer = w[0]
    delta_fin = w[1]

    exp_portfolio_return = delta_beer*(beer_cer-0.01) + delta_fin*(fin_cer-0.01)
    portfolio_variance = (delta_beer**2)*beer_var + (delta_fin**2)*fin_var + 2*delta_fin*delta_beer*beer_fin_cov

    mean_returns.append(exp_portfolio_return)
    risk.append(sqrt(portfolio_variance))

    sharpe = (exp_portfolio_return - 0.01)/float(sqrt(portfolio_variance))
    sharpe_ratio_to_weights[sharpe] = w


max_sharpe_ratio = max( sharpe_ratio_to_weights.keys() )
optimal_weighting = sharpe_ratio_to_weights[max_sharpe_ratio]

print("\n Max Sharpe Ratio: ", max_sharpe_ratio)
print("\n Optimal Weighting: ", optimal_weighting)


plt.plot(risk, mean_returns, 'r-')
plt.xlabel("Standard Deviation")
plt.ylabel("Expected Returns")
plt.title("Portfolio Frontier: Weights Distributed between Beer, Finance")
plt.savefig("hw1_image2.png")
plt.show()
"""










