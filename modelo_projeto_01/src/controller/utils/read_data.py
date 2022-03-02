import pandas as pd

def getCSV():
    data = pd.read_csv('files/data.csv')
    return data

def getJSON():
    data = pd.read_json('files/data.json')
    return data
