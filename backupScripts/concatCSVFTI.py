import os
import csv
import pdb

dataDirName = os.getcwd()

fullInputExtension = "DataForSR.csv"
	#e.g. timeStep_32EPR_2GS_4NS_8Ranks_DataForSR.csv
fullOutputExtension = "FullOutputData.csv"

kernelList = []

#I think this was to remove existing files so appending wouldn't happen...
#for fileName  in os.listdir(dataDirName):
  #if(fileName.endswith(myCSVext)):
    #os.remove(fileName)

for file in os.listdir(dataDirName):
  if(file.endswith(fullInputExtension)):

     parsedFilename = file.split('_')

     kernelName = parsedFilename[0]
     EPR = parsedFilename[1]
     EPR = EPR[0:len(EPR)-8]
     numR = parsedFilename[2]
     numR = numR[0:len(numR)-1]
     NS = parsedFilename[3]
     NS = NS[0:len(NS)-2]
     GS = parsedFilename[4]
     GS = GS[0:len(GS)-6]
     
     kernelList.append(kernelName)
     outputFileName = kernelName + fullOutputExtension

     with open(file) as inputFile:
       data = inputFile.readlines()
    
     if(kernelName in kernelList):
       with open(outputFileName, 'a') as outputFile:
         outputFile.writelines(data)
     else:
       with open(outputFileName, 'w') as outputFile:
         outputFile.writelines(data)
