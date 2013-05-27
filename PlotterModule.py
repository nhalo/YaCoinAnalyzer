#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from matplotlib.pyplot import ioff
from matplotlib.pyplot import ion
from matplotlib.pyplot import legend
from matplotlib.pyplot import twinx
import numpy as np

__author__="nhalo"
__date__ ="$27.05.2013 21:00:00$"

if __name__ == "__main__":
    #plotter was started as main, not as module
    print "Plotter must be called as a module, not as main!"

def plotBarGraph(yacStruct, plotConfig):
    showGraphs = plotConfig.show
    saveGraphs = plotConfig.save
    plotPath   = plotConfig.path
    plotModes  = plotConfig.modes
     
    nr_of_bins = 0
    #bin_size = 10
    bins = []

    days = []
    amountOfCoinsPerIntervallTotal = []
    amountOfCoinsPerIntervallConfirmed = []
    amountOfCoinsPerIntervallUnconfirmed = []

    for day in yacStruct.daily:
        for key, value in day.items():
            days.append(key)
            amountOfCoinsPerIntervallTotal.append(value['totalSaldo'])
            amountOfCoinsPerIntervallConfirmed.append(value['confirmedSaldo'])
            amountOfCoinsPerIntervallUnconfirmed.append(value['unconfirmedSaldo'])

    #Make np-aray of days
    tmpDays = []
    for index, day in enumerate(days):
        tmpDays.append(index)



    d = np.array(tmpDays)

    #Make np-aray of coin amounts
    c_t = np.array(amountOfCoinsPerIntervallTotal)
    c_c = np.array(amountOfCoinsPerIntervallConfirmed)
    c_u = np.array(amountOfCoinsPerIntervallUnconfirmed)

    #Get figure
    fig = plt.figure(1)
    
    #Plot bar diagramm
    plt.bar( d, c_t, color="blue",alpha = 0.75, label="Coins", align='center')
    plt.xlabel("Day")
    plt.ylabel("Mined YaCoins per day")
    plt.xticks(tmpDays, days)


    if showGraphs:
        plt.show()

    if saveGraphs:
        pdf_page = PdfPages(plotPath+"YacDailyAmount.pdf")
        pdf_page.savefig(bbox_inches='tight')
        pdf_page.close()
        
        fig.savefig(plotPath+"YacDailyAmount.eps", format="eps")
        fig.savefig(plotPath+"YacDailyAmount.svg", transparent=True, bbox_inches='tight')

        print("Diagram written to disc!")

    #histogram
    #cdf