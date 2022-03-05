import os
import pandas as pd

CURRENT_PATH = os.path.dirname(__file__)
DATASET_FILE_PATH = os.path.join(CURRENT_PATH, 'files', 'datasets')


def getCSV(dataset_name):
    data = pd.read_csv('files/datasets/' + dataset_name)
    return data


def getJSON():
    data = pd.read_json('files/data.json')
    return data


def openDatasets():
    current_path = os.path.dirname(__file__)

    for x in range(0, 3):
        splitted = os.path.split(current_path)
        current_path = splitted[0]

    dataset_path = os.path.join(splitted[0], 'files', 'datasets')

    dataset_list = os.listdir(dataset_path)

    dataframe_list = []

    for dataset in dataset_list:
        dataframe = getCSV(dataset)
        dataframe_list.append(dataframe)

    return pd.concat(dataframe_list).drop_duplicates().reset_index(drop=True)


def listOfDatasets():
    current_path = os.path.dirname(__file__)

    for x in range(0, 3):
        splitted = os.path.split(current_path)
        current_path = splitted[0]

    dataset_path = os.path.join(splitted[0], 'files', 'datasets')

    dataset_list = os.listdir(dataset_path)
    return dataset_list
