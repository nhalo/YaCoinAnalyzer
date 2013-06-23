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

    if outputType == 'total':
        print "##########################################################"
        print "                     Total income                         "
        print "##########################################################"
        print ""

        print "Income total" + "        : " + str(yacStruct.totalIncome)
        print "Income last 14 days" + " : " + str(yacStruct.last14DaysTotalIncome)

        print ""
        print ""

    if outputType == 'avg':
        print "##########################################################"
        print "                    Average income                        "
        print "##########################################################"
        print ""

        print "Daily average income total" + "        : " + str(yacStruct.avgIncomePerDay)
        print "Daily average income last 14 days" + " : " + str(yacStruct.avgIncomeLast14Days)

        print ""
        print ""