import os
import csv
import pdb

dataDirName = os.getcwd()

fullInputExtension = "DataForSR.csv"
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
     chkptFreq = parsedFilename[1]
     chkptFreq = chkptFreq[0:len(chkptFreq)-3]
     size = parsedFilename[2]
     size = size[0:len(size)-4]
     numCores = parsedFilename[3]
     numCores = numCores[0:len(numCores)-5]
     #fileDict = {}

     kernelList.append(kernelName)
     #temp = fileName.split('Size')[1]
     #runSize = int(temp.split(fullInputExtension)[0])
     outputFileName = kernelName + fullOutputExtension

     with open(file) as inputFile:
       data = inputFile.readlines()
    
     if(kernelName in kernelList):
       with open(outputFileName, 'a') as outputFile:
         outputFile.writelines(data)
     else:
       with open(outputFileName, 'w') as outputFile:
         outputFile.writelines(data)
