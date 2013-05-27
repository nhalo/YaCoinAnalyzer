#!/usr/bin/env python2.7

#Data structure for saving collected yac data
class DataStruct:
    __author__="nhalo"
    __date__ ="$26.05.2013 03:26:00$"

    if __name__ == "__main__":
        print "You must run csv_analyzer!"
        exit(0)

    def __init__(self):

        self.data              = []
        self.daily             = []
        self.totalIncome       = 0.0
        self.avgIncomePerDay   = 0.0

class PlotConfig:
    def __init__(self):

        self.save              = False
        self.show              = False
        self.path              = ""
        self.modes             = []
        self.graphs            = []