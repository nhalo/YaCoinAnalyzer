from DataStructs import DataStruct
from DataStructs import PlotConfig
from csvReader import parseCSV
from DataAnalyzer import analyzeData
from OutputModule import outputConsole
from PlotterModule import plotBarGraph
from PlotterModule import  plotTransactionsTotal
import os
import argparse

__author__="nhalo"
__date__ ="$26.05.2013 03:26:00$"

if __name__ != "__main__":
    exit(0)

#Define commandline switches
def parse_command_line():

    parser = argparse.ArgumentParser(description="CSV Parser")
    parser.add_argument('file_uri', type=str,
                        help='Full path to the file to parse')
    parser.add_argument('-ps', '--plot_and_save', action='store_true',
                        help='Enables graph plotting and saving to disc')
    parser.add_argument('-pv', '--plot_and_view', action='store_true',
                        help='Enables graph plotting and displaying on screen')
    parser.add_argument('-fi', '--filter', type=str, nargs='+',
                        help='Enables a custom filter. Only a coin source with ' 
                              +'this Label will be used')

    return parser.parse_args()

#CSV Analyzer for evaluation of YaCoin Mining Data

#
# main()
#

args = parse_command_line()

modes       = ['daily', 'total', 'avg']
plotGraphs  = ['bar', 'total_trans']
plotLength  = 14

#If the user did set up a filter with -f , then
#only these sources will be counted
usedSources = []
if args.filter == None:
    usedSources.append(args.filter)
else:
    usedSources = args.filter

#getting the file uri
fileUri = args.file_uri

#normalize the path
fileUri = os.path.normpath(fileUri)

#set up empty dataStruct
yacStruct = DataStruct()

#Set up filters
yacStruct.usedSources = usedSources

#load the csv and build yac object
parseCSV(fileUri, yacStruct)

#analyze yac data
analyzeData(yacStruct)

#output analyzed data as text
for mode in modes:
    outputConsole(yacStruct, mode)

#calculate working hours and effective win, loss and costs

#Should we plot something and save it to disc?
doPlotAndSave = args.plot_and_save

#Should we plot something and show it on screen?
doPlotAndView = args.plot_and_view

#Set up plot config struct
if doPlotAndSave or doPlotAndView:
    plotConfig        = PlotConfig()
    plotConfig.path   = os.path.dirname(fileUri)
    plotConfig.modes  = modes
    plotConfig.show   = doPlotAndView
    plotConfig.save   = doPlotAndSave
    plotConfig.length = plotLength
    #plotConfig.graphs = plotGraphs
    
    #Plot data
    for plotGraph in plotGraphs:
        if plotGraph == 'bar':
            plotBarGraph(yacStruct, plotConfig)
        if plotGraph == 'total_trans':
            plotTransactionsTotal(yacStruct, plotConfig)