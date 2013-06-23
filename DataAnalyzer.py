__author__="nhalo"
__date__ ="$26.05.2013 03:26:00$"

def analyzeData(yacStruct):

    actualTotalSaldo        = 0.0
    actualConfirmedSaldo    = 0.0
    actualUnconfirmedSaldo  = 0.0

    #First analyze the daily income
    for index, transaction in enumerate(yacStruct.data):
        if 'Date' in transaction:
            dateOfTransaction = transaction['Date'].split('T')[0]
            if index in range(len(yacStruct.data)-1):
                dateOfNextTransaction = yacStruct.data[index+1]['Date'].split('T')[0]
            else:
                dateOfNextTransaction = 'END'

            #Check if the next transaction is on the same day as the actual
            if dateOfTransaction == dateOfNextTransaction or dateOfNextTransaction == 'END':
                if transaction['Confirmed'] == 'true':
                    actualConfirmedSaldo += float(transaction['Amount'])
                else:
                    actualUnconfirmedSaldo += float(transaction['Amount'])

                actualTotalSaldo += float(transaction['Amount'])

            #This gets triggered, if the next day is approaching and we must save our data. 
            #It also gets triggered by 'END' for the next day to force the data into the structure
            #if it was the last day with data.
            if dateOfTransaction != dateOfNextTransaction or dateOfNextTransaction == 'END':
                yacStruct.daily.append({dateOfTransaction : {'totalSaldo' : actualTotalSaldo , 
                                                             'confirmedSaldo' : actualConfirmedSaldo ,  
                                                             'unconfirmedSaldo' : actualUnconfirmedSaldo}})
                actualTotalSaldo        = 0.0
                actualConfirmedSaldo    = 0.0
                actualUnconfirmedSaldo  = 0.0

    #Analyse the total income, number of days working and average income per day
    totalIncome             = 0.0
    nrOfDays                = 0
    avgIncomePerDay         = 0.0
    last14DaysTotalIncome   = 0.0
    avgIncomeLast14Days     = 0.0
    for day in  yacStruct.daily:
            for key, value in day.items():
                totalIncome += float(value['totalSaldo'])
                nrOfDays    += 1

                if nrOfDays <= 14:
                    last14DaysTotalIncome += float(value['totalSaldo'])

    avgIncomePerDay     = totalIncome / nrOfDays
    avgIncomeLast14Days = last14DaysTotalIncome / 14

    yacStruct.totalIncome     = totalIncome
    yacStruct.nrOfDays        = nrOfDays
    yacStruct.avgIncomePerDay = avgIncomePerDay

    #last 14 days statistics
    yacStruct.last14DaysTotalIncome = last14DaysTotalIncome
    yacStruct.avgIncomeLast14Days   = avgIncomeLast14Days
