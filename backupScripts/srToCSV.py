import os
import csv
import pdb
import numpy as np
from collections import OrderedDict

dataDirName = os.getcwd()

inputExt = "FT.csv"
numIters = "150"

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


kernelList = []
modelDict = OrderedDict()

for fileName  in os.listdir(dataDirName):
  if(fileName.endswith(inputExt)):

    kernelName = fileName.split(".csv")[0]
    kernelList.append(kernelName)
    
    #outputFileName = kernelName + fullOutputExtension

    with open(fileName) as inputFile:
      reader = csv.reader(inputFile)
      data = inputFile.readlines()
      #pdb.set_trace()
      for currLine in data:
        lineNum = currLine.split(',')[0]
        if (lineNum == numIters):
          formula = currLine.split("\"")[1]
          modelDict[kernelName] = formula 
    
print( "size" + ',', end = "")
for key in modelDict:
  print( key + ',', end = "")
print( )
  
for size in range(1,100,1):
  print(str(size) + ',', end = "")
  for key in modelDict:
    print( str(eval(modelDict[key])) + ',', end = "")
  print( )

