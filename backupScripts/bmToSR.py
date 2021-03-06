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

#loop over files in this directory
for file  in os.listdir(dataDirName):
  if(file.startswith(inputPrefix)):

    #Parsing run parameters from file name
      #Note! This section is heavily dependent on file name formate. If it changes, this has to change.
    parsedFilename = file.split('_')
    chkptFreq = parsedFilename[2]
    chkptFreq = chkptFreq[0:len(chkptFreq)-3]
    size = parsedFilename[3]
    size = size[0:len(size)-4]
    numCores = parsedFilename[4]
    numCores = numCores[0:len(numCores)-9]
    
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
        kernelTime = row[1] #time = 2nd token
	
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
      outputCSVFile = kernel+"_"+str(chkptFreq)+"CPF_"+str(size)+"Size_"+str(numCores)+"Cores_" + "DataForSR"  + ".csv"
      with open(outputCSVFile, 'w', newline='') as outputCSV:
        dataWriter = csv.writer(outputCSV, delimiter=',')
      #Add the list to the proper file as a new line
        fileDict[kernel].insert(0,str(numCores)) #Remember, these are all added to the front, so they have to be added in reverse order
        fileDict[kernel].insert(0,str(size))
        fileDict[kernel].insert(0,str(chkptFreq))
        dataWriter.writerow( fileDict[kernel])

