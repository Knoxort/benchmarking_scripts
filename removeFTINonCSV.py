#This file copies any input file starting with the log prefix and outputs it, but does not copy
	#any lines that it does not see as having meaningful output. This includes:
		#Lines that dont have a comma (these should all be csv lines)
		#Lines that include one of the phrases listed below that the perm file spits out
			#cycle
			#time
			#otal
	#Possible improvements
		#Make the list of phrases a list instead
		#Put a tag in lines that you want to keep, instead of csvs

import os
import csv
import pdb

dataDirName = os.getcwd()

lineHeader = "TJL,"
inputPrefix = "log"
outputPrefix = "scrubbed"

for fileName in os.listdir(dataDirName):
  if(fileName.startswith(inputPrefix)):

    outName = outputPrefix + fileName
    
    with open(fileName) as inFile:
      lines = inFile.readlines()

      for currLine in lines:
        if (currLine.startswith(lineHeader)):
          currLine = currLine.replace(lineHeader, '')
          with open(outName, 'a') as outFile:
            outFile.writelines(currLine)

