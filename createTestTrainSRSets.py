import os
import csv
import pdb
import numpy as np
import sys
#Usage: python3 createTestTrainSRSets.py numTotalSamples numTrainingSamples

dataDirName = os.getcwd()

fullInputExtension = "AveragedForSRTool.csv" #aabcfnAveragedForSRTool.csv
trainingOutputExtension = "_trainData.csv"
testingOutputExtension = "_testData.csv"

numDataPoints = int(sys.argv[1])
numTrainingPoints = int(sys.argv[2])
numTestingPoints = numDataPoints - numTrainingPoints


for fileName  in os.listdir(dataDirName):
  if(fileName.endswith(trainingOutputExtension)):
    os.remove(fileName)
  if(fileName.endswith(testingOutputExtension)):
    os.remove(fileName)

for fileName  in os.listdir(dataDirName):
  if(fileName.endswith(fullInputExtension)):

    print("Entering file:" + fileName)

    kernelName = fileName.split("Averaged")[0]
    dataCount = 0
    trainingFile = kernelName + trainingOutputExtension
    testingFile = kernelName + testingOutputExtension
    
    testTrainVector = np.array([0] * numTrainingPoints + [1] * (numDataPoints - numTrainingPoints))
    np.random.shuffle(testTrainVector)

    with open(fileName) as inputFile:
      reader = csv.reader(inputFile)
      data = inputFile.readlines()
      rowIndex = 0  
      for dataRow in data:
        
        #pdb.set_trace()
        if ( testTrainVector[rowIndex] == 0 ):  #This is a training point
          with open(trainingFile, 'a') as outputFile:
            outputFile.writelines(dataRow)
        else: 					                        #This is a testing point
          with open(testingFile, 'a') as outputFile:
            outputFile.writelines(dataRow)

        rowIndex = rowIndex + 1
        dataCount = dataCount + 1

      if ( dataCount != numDataPoints ):
        print("Error: number of lines in file doesn't match up with CLA for size! Exiting...)")
        exit()

  
