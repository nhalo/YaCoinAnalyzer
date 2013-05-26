__author__="nhalo"
__date__ ="$26.05.2013 03:26:00$"

def outputConsole(yacStruct, outputType):
    if outputType == 'daily':
        print "##########################################################"
        print "               Summary of daily income                    "
        print "##########################################################"
        print ""

        for day in  yacStruct.daily:
            for key, value in day.items():
                print str(key) + " : " + str(value)

        print ""
        print ""

    if outputType == 'dailyAvg':
        print "##########################################################"
        print "       Average daily income based on total saldo         "
        print "##########################################################"
        print ""

        print "Daily average income" + " : " + str(yacStruct.avgIncomePerDay)

        print ""
        print ""