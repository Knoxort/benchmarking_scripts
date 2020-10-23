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
#example log_luleshFTI_20RankSize_27GS_1NS_27Ranks.txt

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
   
    #pdb.set_trace()
 
    fileDict = {}

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
      for row in dataProcessor:
        kernelName = row[0] #kName =  1st token
        kernelTime = row[3] #time = 2nd token
	
	#If kName is already a dictionary key
        if kernelName in fileDict:
          fileDict[kernelName].append(kernelTime)
          
	#Right now, going off the assumption that the size is unique to every file. Therefore, the size doesn't have to be kept as a variable
	#if not
        else:
          fileDict[kernelName] = []
          fileDict[kernelName].append(kernelTime)

    #At this point, all the times and kernels for this file (i.e. this size) should be in the dictionary. All we gotta do is print them out now.

    #All of these should be going into the same file

    #For each key in the dictionary (each kernel that is timed)
    for kernel in fileDict:
      outputCSVFile = kernel+"_"+str(EPR)+"EPR_"+str(numR)+"Ranks_"+str(NS)+"NS_"+str(GS)+"GS_DataForSR.csv"
      with open(outputCSVFile, 'w', newline='') as outputCSV:
        dataWriter = csv.writer(outputCSV, delimiter=',')
      #Add the parameter values to the file to the beginning of the file
        fileDict[kernel].insert(0,str(GS))
        fileDict[kernel].insert(0,str(NS))
        fileDict[kernel].insert(0,str(numR)) #Remember, these are all added to the front, so they have to be added in reverse order
        fileDict[kernel].insert(0,str(EPR))
        dataWriter.writerow( fileDict[kernel])

