import os
import csv
import pdb
import sys


dataDirName = os.getcwd()

fullInputExtension = "FullOutputData.csv" #aabcfnFullOutputData_my.csv
fullOutputExtension = "AveragedForSRTool.csv"
statFileName = "statsFile.csv"

kernelList = []
numParams = int(sys.argv[1]) #The number of parameters, after which we can start averaging data
timeMult = int(sys.argv[2]) #If we want the multiple in microseconds or anything
    
#statLine='EPR'+','+'numR'+','+'NS'+'GS'+','+'average'+','+'dataCount'+','+'errorCount'+','+'\n'
statLine='EPR'+','+'numR'+','+'NS'+'GS'+','+'average'+','+'dataCount'+','+'errorCount'+','+'\n'
with open(statFileName, 'w') as statFile:
  statFile.writelines(statLine)

for fileName  in os.listdir(dataDirName):
  if(fileName.endswith(fullOutputExtension)):
    os.remove(fileName)

for fileName  in os.listdir(dataDirName):
  if(fileName.endswith(fullInputExtension)):

    kernelName = fileName.split('Full')[0]
    kernelList.append(kernelName)
    outputFileName = kernelName + 'timeMult' + str(timeMult)  + fullOutputExtension
   
    print("Entering File " + fileName)
 
    with open(fileName) as inputFile:
      reader = csv.reader(inputFile)
      data = inputFile.readlines()
      for dataRow in data:
        average = 0
        dataCount = 0
        errorCount = 0
        currRow = dataRow.split(",")
        for i in range(numParams,len(currRow)):
          try:
            average = average + float(currRow[i])
            dataCount = dataCount + 1
          except ValueError:
            print("There was a ValueError with this value: " + currRow[i])  
            errorCount = errorCount + 1
        average = average / float(dataCount) * timeMult

        #if( (currRow[0] == '25') and (currRow[1] == '8')):
          #pdb.set_trace()
        statLine=kernelName+','+currRow[0]+','+currRow[1]+','+str(dataCount)+','+str(+errorCount)+','+'\n'
        with open(statFileName, 'a') as statFile:
          statFile.writelines(statLine)
        #outputLine=str(dataCount)+','+currRow[0]+','+currRow[1]+','+currRow[2]+','+str(average)+'\n'  #Need to find a way to loop over the parameters, instead of hard coding printing them thre times
        outputLine=currRow[0]+','+currRow[1]+','+str(average)+'\n'  #Need to find a way to loop over the parameters, instead of hard coding printing them thre times
  
        if(kernelName in kernelList):
          with open(outputFileName, 'a') as outputFile:
            outputFile.writelines(outputLine)
        else:
          with open(outputFileName, 'w') as outputFile:
            outputFile.writelines(outputLine)

#    statLine=currRow[0]+','+currRow[1]+','+currRow[2]+','+currRow[3]+','+str(average)+','+str(dataCount)+','+str(+errorCount)+','+'\n'
#    with open(statFileName, 'a') as statFile:
#      statFile.writelines(statLine)
