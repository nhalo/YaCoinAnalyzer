import csv
__author__="nhalo"
__date__ ="$26.05.2013 03:26:00$"

def parseCSV(fileUri, yacStruct):
    file = ""
    isTagLine = True

    #All recognized Tags
    supportedTags = ['Confirmed', 'Date', 'Label',
                        'Address', 'Amount', 'Id']
    tagsFound = []

    #Open the csv file and read it
    with open(fileUri, 'rb') as csvfile:
        csvFile = csv.reader(csvfile, delimiter=',', quotechar='"')

        #Parse every line of the file till end
        for row in csvFile:
            dataRowData = {}
            for index, data in enumerate(row):
                if(isTagLine):
                    tagsFound.append(data)
                else:
                    if tagsFound[index] in supportedTags:
                        dataRowData[tagsFound[index]] = data
            if len(dataRowData) == 0:
                isTagLine = False
            else:
                yacStruct.data.append(dataRowData)