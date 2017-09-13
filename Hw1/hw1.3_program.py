import numpy as np
import matplotlib.pyplot as plt
import cvxopt as opt
from cvxopt import blas, solvers
import pandas as pd

def optimal_portfolio( returns ):

    n = len(returns)  # Number of assets
    returns = np.asmatrix(returns)

    N = 500
    mus = [10 ** (5.0 * t / N - 1.0) for t in range(N)]

    # Convert to cvxopt matrices
    S = opt.matrix(np.cov(returns))
    pbar = opt.matrix(np.mean(returns, axis=1))

    # Create constraint matrices
    G = -opt.matrix(np.eye(n))  # negative n x n identity matrix
    h = opt.matrix(0.0, (n, 1))
    A = opt.matrix(1.0, (1, n))
    b = opt.matrix(1.0)

    # Calculate efficient frontier weights using quadratic programming
    portfolios = [solvers.qp(mu * S, -pbar, G, h, A, b)['x'] for mu in mus]

    # CALCULATE RISKS AND RETURNS FOR FRONTIER
    returns = [blas.dot(pbar, x) for x in portfolios]
    risks = [np.sqrt(blas.dot(x, S * x)) for x in portfolios]

    # CALCULATE THE 2ND DEGREE POLYNOMIAL OF THE FRONTIER CURVE
    m1 = np.polyfit(returns, risks, 2)
    x1 = np.sqrt(m1[2] / m1[0])

    # CALCULATE THE OPTIMAL PORTFOLIO
    wt = solvers.qp(opt.matrix(x1 * S), -pbar, G, h, A, b)['x']

    return np.asarray(wt), returns, risks



# Turn off progress printing
solvers.options['show_progress'] = False

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
## assetList.append(market_rates)
assetList.append(aero_rates)
assetList.append(guns_rates)
assetList.append(steel_rates)
assetList.append(ships_rates)
assetList.append(beer_rates)
assetList.append(toys_rates)
assetList.append(fin_rates)
assetList.append(rtail_rates)

return_vec = np.array(assetList)
weights, returns, risks = optimal_portfolio(return_vec)

print("optimal weights\n")
for elm in weights:

    print(elm)

print("\n")

plt.ylabel('mean')
plt.xlabel('std')
plt.plot(risks, returns, 'r-o')
plt.savefig("hw1_image3.png")
plt.show()

