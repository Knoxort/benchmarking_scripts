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
    numCores = numCores[0:len(size)-11]
    pdb.set_trace()

    fileDict = {}

    currFileFullPath = os.path.join(dataDirName, filename)
    currFile = os.path.basename(currFileFullPath)
    #print(currFile)
    with open(currFile, newline='') as csvfile:
      bmReader = csv.reader(csvfile, delimiter = ',')
    fileName = os.path.splitext(currFile)[0]	#Removes extension
    #print(os.path.join(dataDirName, filename))
    runSize = fileName[-2:0] #size = from file name
    runSize = int(currFile[-10:-8]) #size = from file name
	#THis line assumes all log files follow this naming format:
		#formattedlulesh_#Cores_##Size.log
    #print(runSize)
    #loop over lines in this file
    with open(currFile) as csvfile:
      dataProcessor = csv.reader(csvfile, delimiter=',')
      rowCount = 0

      #for each line
      for row in dataProcessor:
        #pdb.set_trace()
        #currRow = next(dataProcessor)
        #print(rowCount)
        #print(currRow)

        #if(rowCount > 4):
        #  break
        #else:
        rowCount = rowCount + 1

        #kernelName = currRow[0] #kName =  1st token
        kernelName = row[0] #kName =  1st token
        #kernelTime = currRow[1] #time = 2nd token
        kernelTime = row[1] #time = 2nd token
	
	#If kName is already a dictionary key
        if "cycle" in kernelName:
          pdb.set_trace()
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
      break
      outputCSVFile = kernel + "Size" + str(runSize) + "Freq" + str(crFreq) + "DataForSR"  + ".csv"
      if "cycle" in  outputCSVFile:
        pdb.set_trace()
      with open(outputCSVFile, 'w', newline='') as outputCSV:
        #dataWriter = csv.writer(outputCSVFile, delimiter=',')
        dataWriter = csv.writer(outputCSV, delimiter=',')
      #Add the list to the proper file as a new line
        #dataWriter.writerow( str(runSize) + fileDict[kernel])
        fileDict[kernel].insert(0,str(runSize))
        #dataWriter.writerow( str(runSize) + fileDict[kernel])
        dataWriter.writerow( fileDict[kernel])

pdb.set_trace()
