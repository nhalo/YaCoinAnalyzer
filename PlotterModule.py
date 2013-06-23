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
    amountOfCoinsPerIntervallTotal          = []
    amountOfCoinsPerIntervallConfirmed      = []
    amountOfCoinsPerIntervallUnconfirmed    = []

    #averageDailyIncomeTotal                      = yacStruct.avgIncomePerDay 
    averageDailyIncomeLast14Days                 = yacStruct.avgIncomeLast14Days

    for index, day in enumerate(yacStruct.daily):
        if index+1 <= plotConfig.length:
            for key, value in day.items():
                days.append(key)
                amountOfCoinsPerIntervallTotal.append(value['totalSaldo'])
                amountOfCoinsPerIntervallConfirmed.append(value['confirmedSaldo'])
                amountOfCoinsPerIntervallUnconfirmed.append(value['unconfirmedSaldo'])

    #Make np-aray of days
    tmpDays = []
    tmpInc  = []
    for index, day in enumerate(days):
        tmpDays.append(index)
        tmpInc.append(averageDailyIncomeLast14Days)

    d = np.array(tmpDays)

    #Make np-aray of coin amounts
    c_t = np.array(amountOfCoinsPerIntervallTotal)
    c_c = np.array(amountOfCoinsPerIntervallConfirmed)
    c_u = np.array(amountOfCoinsPerIntervallUnconfirmed)

    a_i = np.array(tmpInc)

    #Get figure
    fig = plt.figure(1)
    
    #Plot bar diagramm
    p1 = plt.bar( d, c_u, color="red",alpha = 0.75, label="unconfirmed", align='center')
    p2 = plt.bar( d, c_c, color="blue",alpha = 0.75, label="confirmed", align='center', bottom=c_u)

    #Plot average daily income
    p3 = plt.plot( d, a_i,'k--', alpha = 0.75, label="daily avg")

    #Rotate x-axis
    fig.autofmt_xdate()


    plt.xlabel("Days")
    plt.ylabel("Mined YaCoins")
    plt.xticks(tmpDays, days)

    #Add legend
    plt.legend()

    if saveGraphs:
        pdf_page = PdfPages(plotPath+"YacDailyAmountLast14Days.pdf")
        pdf_page.savefig(bbox_inches='tight')
        pdf_page.close()
        
        fig.savefig(plotPath+"YacDailyAmountLast14Days.eps", format="eps")
        fig.savefig(plotPath+"YacDailyAmountLast14Days.svg", transparent=True, bbox_inches='tight')

        print("Diagram written to disc!")

    if showGraphs:
        plt.show()

    fig.clear()

def plotHistogramm():
    pass

def plotTransActionsOverTime():
    pass

def plotTransactionsTotal(yacStruct, plotConfig):
    showGraphs                  = plotConfig.show
    saveGraphs                  = plotConfig.save
    plotPath                    = plotConfig.path
    plotModes                   = plotConfig.modes
     
    nrOfTransactions            = 0
    amountOfSingleTransactions   = []

    for transaction in yacStruct.data:
        amountOfSingleTransactions.append(transaction['Amount'])

    nrOfTransactions = amountOfSingleTransactions.__len__()

    n_t = np.arange(1, nrOfTransactions+1)
    a_t = np.array(amountOfSingleTransactions)

    #Get figure
    fig = plt.figure(1)
    
    #Plot curve diagramm
    p1 = plt.plot( n_t, a_t,'b-', alpha = 0.75)
    plt.xlabel("Number of Transactions")
    plt.ylabel("Mined YaCoins")

    if saveGraphs:
        pdf_page = PdfPages(plotPath+"YactransactionTotal.pdf")
        pdf_page.savefig(bbox_inches='tight')
        pdf_page.close()
        
        fig.savefig(plotPath+"YactransactionTotal.eps", format="eps")
        fig.savefig(plotPath+"YactransactionTotal.svg", transparent=True, bbox_inches='tight')

        print("Diagram written to disc!")

    if showGraphs:
        plt.show()

    fig.clear()

    
    
    #histogram
    #cdf