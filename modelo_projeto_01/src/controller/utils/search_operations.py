import pandas as pd

from exceptions import FilterOperationUnavailable

CAR_VALUE_COLUMN_NAME = 'car_value'
CAR_MAKE_COLUMN_NAME = 'car_make'
CITY_COLUMN_NAME = 'city'

def group_by():
    # TODO: implement function following:
    # https://github.com/AlanRicardoS/devops-tools-grupo-04/issues/14
    return None

def filter_by(dataset, reference_column, filter_value):

    if (reference_column == CAR_MAKE_COLUMN_NAME):
        filtered_df = dataset.drop(dataset[dataset.car_make != filter_value].index)
        
    elif (reference_column == CITY_COLUMN_NAME):
        filtered_df = dataset.drop(dataset[dataset.city != filter_value].index)
    
    else:
        raise FilterOperationUnavailable("Filter not available for requested column", reference_column)

    grouped_df = filtered_df.groupby([reference_column]).mean()
    car_value_mean = grouped_df[[CAR_VALUE_COLUMN_NAME]]

    return car_value_mean