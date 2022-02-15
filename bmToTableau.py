#This file organizes the data so that it's sorted by kernel and run size. However, it now has to be sorted so that it knows the 
import os
import csv
import pdb

dataDirName = os.getcwd()

#Dictionary 
	#Keys are the 
benchmarkMPIDict = {}
benchmarkPermDict = {}

inputPrefix = "scrubbed" #e.g. scrubbedlog_lulesh_10CPF_10Size_1Cores.txt

print("Enter the name of the output file, no extensions")
temp = str(input())
outputFile = temp + ".csv"
#example log_luleshFTI_20RankSize_27GS_1NS_27Ranks.txt

lineList = []
#loop over files in this directory
for file  in os.listdir(dataDirName):
  if(file.startswith(inputPrefix)):

    #Parsing run parameters from file name
      #Note! This section is heavily dependent on file name formate. If it changes, this has to change.
    parsedFilename = file.split('_')
    EPR = parsedFilename[2]
    EPR = EPR[0:len(EPR)-3]
    numR = parsedFilename[3]
    numR = numR[0:len(numR)-1]
    NS = parsedFilename[4]
    NS = NS[0:len(NS)-2]
    GS = parsedFilename[5]
    GS = GS[0:len(GS)-6]
    
    print("Processing file: " + file) 

#After getting the file name, I shouldn't need an output file dict anymore. Basically, I want to
	#Add all the lines to the new file
	#Insert the file statistics (e.g. NS, and GS) into the line
 
    metaFlag = 1

    #currFileFullPath = os.path.join(dataDirName, filename)
    currFileFullPath = os.path.join(dataDirName, file)
    currFile = os.path.basename(currFileFullPath)
    with open(currFile, newline='') as csvfile:
      bmReader = csv.reader(csvfile, delimiter = ',')
    fileName = os.path.splitext(currFile)[0]	#Removes extension
    
    #loop over lines in this file
    with open(currFile) as csvfile:
      dataProcessor = csv.reader(csvfile, delimiter=',')


      #for each line
      for row in dataProcessor:		#Note: The first row is the metadata, and may need to be handled differently
	#Add the items to the row first
        if metaFlag == 1:
          row.insert(1,"GS")
          row.insert(1,"NS")
          row.insert(1,"numR")
          row.insert(1,"EPR")
          metaFlag = 0
        else:
          row.insert(1,GS)
          row.insert(1,NS)
          row.insert(1,numR)
          row.insert(1,EPR)
        lineList.append(row)
with open(outputFile, 'w') as f:
  write = csv.writer(f)

  write.writerows(lineList)
  #Ok, at this point, everything should be in the list. All we need to do is save the file as a csv
