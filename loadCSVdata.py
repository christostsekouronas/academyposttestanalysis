import pandas as pd



def loadTest(filepath):
    df = pd.read_csv(filepath)
    return df.to_string()