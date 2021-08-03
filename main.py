# Actions
#
# Read Configuration file
# Load Data
# Print Data

import config as configLoader
import loadCSVdata as dataLibrary

allConfigKeys = configLoader.loadConfig()

data = dataLibrary.loadTest(allConfigKeys["datasetfile"])

# Print grade based on surname
import pandas as pd

df = pd.read_csv('data-utf8.csv')

print(df.head(10))


#if allConfigKeys["reportOnRead"]:
    #print(data)
#else:
    #print("No report is configured")

