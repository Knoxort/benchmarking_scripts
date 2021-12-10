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
inFileExt = "Model.txt"
outFileExt = "Table.csv"
srDelimit = "Program: " #I have no idea why the delimiter was Program... Gotta be a misreplace
srDelimit = "\""
paramStep = 4
paramStart = 2



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
          #pdb.set_trace()
        except IndexError:	#I totally forgot why this is here... something about getting the formula right...
          print("Skipping this")
    
      with open(outputFile, 'a') as outPipe:
          #outPipe.writelines(str(size) + "," + str(eval(formula)) + "\n")
          outPipe.writelines("cpf,size,numCores,time\n")

          #pdb.set_trace()

#Sometime that is not today, we'll go into how to have a variable number of nexted loops
	#Could make the x number of parameter lists in a larger list, and then loop over all of them?
          #Loop over CPF
          for i in range (1,2,1):
            #Loop over size
            CPF = i
            for j in range (0,12,1):
              #Loop over numCores
              Size = 2**j
              for k in range(1,12,1):
                Cores = k**3
                outPipe.writelines(str(CPF) + "," + str(Size) + "," + str(Cores) + "," + str(eval(formula)) + "\n")
