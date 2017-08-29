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
import matplotlib.pyplot as plt
from itertools import accumulate ## Use this to get the sum of elements in an iterable
from datetime import datetime

## Overall structure for the entire time series
date_list = list()
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

        data_date = L[1] + "-" + L[2] + "-" + L[0]
        date = datetime.strptime(data_date, '%m-%d-%Y').date()
        date_list.append(date)

        #date_to_data[date] = L[3:]

        rf_rates.append(float(L[3]))
        market_rates.append(float(L[4]))
        aero_rates.append(float(L[5]))
        guns_rates.append(float(L[6]))
        steel_rates.append(float(L[7]))
        ships_rates.append(float(L[8]))
        beer_rates.append(float(L[9]))
        toys_rates.append(float(L[10]))
        fin_rates.append(float(L[11]))
        rtail_rates.append(float(L[12]))

line1, = plt.plot_date(date_list, list(accumulate(rf_rates)), 'r-', label = 'RiskFree')
line2, = plt.plot_date(date_list, list(accumulate(market_rates)), 'b-', label = 'Market')
line3, = plt.plot_date(date_list, list(accumulate(aero_rates)), 'g-', label = 'Aero')
line4, = plt.plot_date(date_list, list(accumulate(guns_rates)), 'c-', label = 'Guns')
line5, = plt.plot_date(date_list, list(accumulate(steel_rates)), 'y-', label = 'Steel')
line6, = plt.plot_date(date_list, list(accumulate(ships_rates)), 'm-', label = 'Ships')
line7, = plt.plot_date(date_list, list(accumulate(beer_rates)), 'k-', label = 'Beer')
line8, = plt.plot_date(date_list, list(accumulate(toys_rates)), 'r:', label = 'Toys')
line9, = plt.plot_date(date_list, list(accumulate(fin_rates)), 'b:', label = 'Fin')
line10, = plt.plot_date(date_list, list(accumulate(rtail_rates)), 'g:', label = 'Rtail')

plt.legend(handles=[line1,line2,line3,line4,line5,line6,line7,line8,line9,line10])
plt.xlabel("Time")
plt.ylabel("Log Returns")
plt.title("Log Returns (8 Assets, Market, Risk-Free Rate) over 1975-2017")
plt.savefig("hw1_image1.png")
plt.show()
