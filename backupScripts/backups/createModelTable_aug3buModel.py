from copy import deepcopy
import numpy as np
import math
import os
import csv
import pdb
import sys

def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def div(a,b):
    return (a/b)
def square (a):
    return (a*a)
def cube (a):
    return (a*a*a)
def ln(a):
    return (np.log(a))
def exp(a):
    return (math.exp(a))

currDir = os.getcwd()
inFileExt = "_model.txt"
outFileExt = "BespokeTable.csv"
srDelimit = "Program: " #I have no idea why the delimiter was Program... Gotta be a misreplace
srDelimit = "\""
paramStep = 4
paramStart = 2

#Usage: python3 createModelTable.py numberOfParametersinModel param1 start stop step param2 start stop step etc 
	#For now, arg list is: 2) CPF 6) Size 10) numCores
#if ( ((len(sys.argv)%paramStep) - paramStart) != 0):
#  sys.exit("The argument list does not contain the proper multiple; please recheck and try again.")

#paramCount = int(sys.argv[1])
#paramList = [] #This list will hold the name and list of params
			#The name of a param should always be a "multiple of 4 (0, 4, 8, etc)
			#nameIndex + 1 = start
			#nameIndex + 2 = stop
			#nameIndex + 1 = step

#for i in range(paramStart, len(sys.argv), paramStep):
#  paramList.append(sys.argv[i])

#Delete the current table files
#for fileName in os.listdir(currDir):
#  if(fileName.endswith(outFileExt)):
#    os.remove(fileName)

#For all files in directory that match the in file extension
for fileName in os.listdir(currDir):
  if(fileName.endswith(inFileExt)):
  
    kernelName = fileName.split(inFileExt)[0]
    outputFile = kernelName + outFileExt
    #Start reading the file from the bottom
    with open(fileName) as inputFile:
      srOutput = inputFile.readlines()
      for nextLine in srOutput:
        try:
          #formula = "(\"" + nextLine.split(srDelimit)[1] + "\")"
          formula = str.rstrip(nextLine.split(srDelimit)[1])
        except IndexError:	#I totally forgot why this is here... something about getting the formula right...
          print("Skipping this")
    
      with open(outputFile, 'a') as outPipe:
          #outPipe.writelines(str(size) + "," + str(eval(formula)) + "\n")
          outPipe.writelines("cpf,size,numCores,time\n")

#Sometime that is not today, we'll go into how to have a variable number of nested loops
	#Could make the x number of parameter lists in a larger list, and then loop over all of them?
          cpfList =   [1,10]
          sizeList =  [5, 10, 20, 40, 50, 75, 90]
          coresList = [1, 8, 27, 64, 125]

          #Loop over CPF
          #for CPF in range (int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])):
          for CPF in cpfList:
            #Loop over size
            #for Size in range (int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9])):
            for Size in sizeList:
              #Loop over numCores
              #for Cores in range (int(sys.argv[11]), int(sys.argv[12]), int(sys.argv[13])):
              for Cores in coresList:
                outPipe.writelines(str(CPF) + "," + str(Size) + "," + str(Cores) + "," + str(eval(formula)) + "\n")
     
        

