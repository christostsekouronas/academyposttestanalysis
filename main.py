# Actions
#
# Read Configuration file
# Load Data
# Print Data

import config as configLoader
import loadCSVdata as dataLibrary
import dataanalysis

allConfigKeys = configLoader.loadConfig()

data = dataLibrary.loadTest(allConfigKeys["datasetfile"])

# data is type of DataFrame array. 
# with loc function we get the N element of this array. 
# In each element can be searched as Dictionary. Keys are the Column names of the csv file. 

# get number of rows using len function


if allConfigKeys["PrintGradeBasedOnSurname"]:
    grade = dataanalysis.getGradeBySurname(
        data,
        allConfigKeys["GradeBasedOnSurname"],
        allConfigKeys["WhichAttempt"],
    )
    print(grade)

if allConfigKeys["PrintGradeBasedOnName"]:
    grade = dataanalysis.getGradeBySurname(
        data,
        allConfigKeys["GradeBasedOnSurname"],
        allConfigKeys["WhichAttempt"],
    )
    print(grade)