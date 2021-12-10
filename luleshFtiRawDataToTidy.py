
#This file will run through all the log files in a directory and 
#process them into the tinydata csv format following this 

#Run_Date_and_Time,groupSize,nodeSize,numberOfRanks,elementsPerRank,kernel,runtime

#Input files:
	#All files in the current directory matching the prefix

#Output file:
	

import os
import csv
import pdb
from datetime import datetime

dataDirName = os.getcwd() 	#Save the current directory

lineHeader = "TJL"
inputPrefix = "log_luleshFTI_" #Filename example: log_luleshFTI_Jan18_2EPR_2GS_1NS_2R.txt

index = 2
outputFile = "luleshFtiTinyData_"+ str(datetime.now()) + ".csv"
outputFile = "bmData_luleshFTI__"+ str(datetime.now()) + ".csv"
dateTimeString = str(datetime.now())

headerString = "dateTime,groupSize,nodeSize,numRanks,epr,kernel,measuredTime"

for currFileName in os.listdir(dataDirName):
  if(currFileName.startswith(inputPrefix)):

    parsedInputFilename = currFileName.split('_')	
    epr = parsedInputFilename[index]
    epr = epr[0:len(epr)-len("EPR")] 
    gs = parsedInputFilename[index+1]
    gs = gs[0:len(gs)-len("GS")]
    ns = parsedInputFilename[index+2]
    ns = ns[0:len(ns)-len("NS")]
    #pdb.set_trace() 
    ranks = parsedInputFilename[index+3]
    ranks = ranks[0:len(ranks)-len("R")]

    with open(currFileName) as currFile:
      
      lines = currFile.readlines()

      for currLine in lines:
        if (currLine.startswith(lineHeader)):
          replacedLine = [dateTimeString.replace(' ', '_'), gs, ns, ranks, epr]
          parsedLine = currLine.split(',')	 
          replacedLine.insert(len(replacedLine), parsedLine[1])
          replacedLine.insert(len(replacedLine), parsedLine[2])
          replacedLine.insert(len(replacedLine), parsedLine[3])
          replacedLine.insert(len(replacedLine), parsedLine[4].strip('\n').strip(' '))

          with open(outputFile, 'a', newline='') as outputLog:
            dataWriter = csv.writer(outputLog, delimiter=',')
            dataWriter.writerow(replacedLine)
