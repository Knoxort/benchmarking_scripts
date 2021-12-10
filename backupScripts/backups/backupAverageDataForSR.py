import os
import csv
import pdb

dataDirName = os.getcwd()

fullInputExtension = "FullOutputData_my.csv" #aabcfnFullOutputData_my.csv
fullOutputExtension = "AveragedForSRTool.csv"
myCSVext = "_my.csv"

kernelList = []

for fileName  in os.listdir(dataDirName):
  if(fileName.endswith(fullOutputExtension)):
    os.remove(fileName)

for fileName  in os.listdir(dataDirName):
  if(fileName.endswith(fullInputExtension)):

    kernelName = fileName.split('Full')[0]
    kernelList.append(kernelName)
    outputFileName = kernelName + fullOutputExtension
    
    with open(fileName) as inputFile:
      reader = csv.reader(inputFile)
      data = inputFile.readlines()
      for dataRow in data:
        average = 0
        dataCount = 0
        currRow = dataRow.split(",")
        #pdb.set_trace()
        for i in range(1,len(currRow)):
          average = average + float(currRow[i])
          dataCount = dataCount + 1
        average = average / float(dataCount)
        outputLine = currRow[0] + ',' + str(average) + '\n'
        #pdb.set_trace()
          
        if(kernelName in kernelList):
          with open(outputFileName, 'a') as outputFile:
            outputFile.writelines(outputLine)
        else:
          with open(outputFileName, 'w') as outputFile:
            outputFile.writelines(outputLine)
