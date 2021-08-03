import pandas as pd
import config as configLoader


def loadTest():
    config = configLoader.readConfig()
    #print(config["datasetfile"])
    df = pd.read_csv(config["datasetfile"])
    return df.to_string()