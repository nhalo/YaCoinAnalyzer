from DataStructs import DataStruct
from csvReader import parseCSV
from DataAnalyzer import analyzeData
from OutputModule import outputConsole
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

    return parser.parse_args()

#CSV Analyzer for evaluation of YaCoin Mining Data

#
# main()
#

args = parse_command_line()

#getting the file uri
fileUri = args.file_uri

#normalize the path
fileUri = os.path.normpath(fileUri)

#set up empty dataStruct
yacStruct = DataStruct()

#load the csv and build yac object
parseCSV(fileUri, yacStruct)

#analyze yac data
analyzeData(yacStruct)

#output analyzed data as text
outputConsole(yacStruct, "daily")
outputConsole(yacStruct, "dailyAvg")

#calculate working hours and effective win, loss and costs

#plot diagrams
#bar graph
#histogram
#cdf