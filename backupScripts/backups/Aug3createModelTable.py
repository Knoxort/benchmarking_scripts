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
outFileExt = "Table.csv"
srDelimit = "Program: "
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
        except IndexError:
          print("Skipping this")
    
      with open(outputFile, 'a') as outPipe:
        for size in range(start,stop,step):
          outPipe.writelines(str(size) + "," + str(eval(formula)) + "\n")
     
        
#Sometime that is not today, we'll go into how to have a variable number of nexted loops

#Loop over CPF
for cpf in range (sys.argv[3], sys.arv[4], sys.arg[5]):
  #Loop over size
  for cpf in range (sys.argv[7], sys.arv[8], sys.arg[9]):
    #Loop over numCores
    for cpf in range (sys.argv[11], sys.arv[12], sys.arg[13]):
      print (str(size) + "," + str(eval(formula)))
