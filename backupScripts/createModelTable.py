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

#Usage: python3 createModelTable.py numberOfParametersinModel param1 start stop step param2 start stop step etc 
	#For now, arg list is: 2) CPF 6) Size 10) numCores
if ( ((len(sys.argv)%paramStep) - paramStart) != 0):
  sys.exit("The argument list does not contain the proper multiple; please recheck and try again.")

paramCount = int(sys.argv[1])
paramList = [] #This list will hold the name and list of params
			#The name of a param should always be a "multiple of 4 (0, 4, 8, etc)
			#nameIndex + 1 = start
			#nameIndex + 2 = stop
			#nameIndex + 1 = step

for i in range(paramStart, len(sys.argv), paramStep):
  paramList.append(sys.argv[i])

ampfe_model = ("add(add(add(mul(div(add(mul(ln(add(mul(size, 1.00000000572), -4.36192799144e-08)), 207.041008439), -526.831136616), mul(add(mul(mul(size, add(add(mul(cube(add(mul(size, 0.999999999999), 8.03391191304e-12)), 1.00000207874), -0.00722552604983), add(mul(size, 0.999999999605), 8.0274364164e-09))), 1.00001865431), -350211.737777), add(mul(size, 1.13187335307), -1.75306589206))), 1.0), 1.02070541675e-17), add(mul(square(add(mul(square(add(mul(size, 0.00665995745828), add(mul(cube(mul(square(add(mul(size, 1.01478421122), -0.511684092329)), 0.999999976086)), -5.1363176645e-18), 0.00201814553701))), 0.999059977632), 3.6309656316e-05)), 1.0), 1.96826937195e-18)), -4.33680868994e-19)")

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

          pdb.set_trace()

#Sometime that is not today, we'll go into how to have a variable number of nexted loops
	#Could make the x number of parameter lists in a larger list, and then loop over all of them?
          #Loop over CPF
          for CPF in range (int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])):
            #Loop over size
            for Size in range (int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9])):
              #Loop over numCores
              for Cores in range (int(sys.argv[11]), int(sys.argv[12]), int(sys.argv[13])):
                outPipe.writelines(str(CPF) + "," + str(Size) + "," + str(Cores) + "," + str(eval(formula)) + "\n")
