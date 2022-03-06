import os
import pandas as pd

def getCSV(dataset_name):
    data = pd.read_csv('files/datasets/' + dataset_name)
    return data


def getJSON():
    data = pd.read_json('files/data.json')
    return data

def listOfDatasets():
    # Retrieving current path
    current_path = os.path.dirname(__file__)

    # Extracting root path for 'files' folder
    for x in range(0, 3):
        splitted = os.path.split(current_path)
        current_path = splitted[0]

    # Adding datasets folder suffix path to root path
    dataset_path = os.path.join(splitted[0], 'files', 'datasets')

    # Retrieving a list of all csv files at datasets folder
    dataset_list = os.listdir(dataset_path)

    return dataset_list

def openDatasets():
    dataset_list = listOfDatasets()

    dataframe_list = []

    # Feeding the dataframe list with all csv files at datasets folder
    for dataset in dataset_list:
        dataframe = getCSV(dataset)
        dataframe_list.append(dataframe)

    # Merging all dataframes into a single one
    return pd.concat(dataframe_list).drop_duplicates().reset_index(drop=True)
