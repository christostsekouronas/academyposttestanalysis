import pandas as pd



def loadTest(filepath):
    df = pd.read_csv(filepath)
    return df