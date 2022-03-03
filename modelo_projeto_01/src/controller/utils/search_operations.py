import pandas as pd

from exceptions import FilterOperationUnavailable

CAR_VALUE_COLUMN_NAME = 'car_value'
CAR_MAKE_COLUMN_NAME = 'car_make'
CITY_COLUMN_NAME = 'city'

def group_by(dataset, group_value):
    try:
        grouped = dataset.groupby(group_value).mean()
        car_value_mean = grouped[[CAR_VALUE_COLUMN_NAME]]
    except:
        raise FilterOperationUnavailable("Could not group by dataset using " + group_value)
    return car_value_mean

def filter_by(dataset, reference_column, filter_value):

    if (reference_column == CAR_MAKE_COLUMN_NAME):
        filtered_dataset = dataset.drop(dataset[dataset.car_make != filter_value].index)
        
    elif (reference_column == CITY_COLUMN_NAME):
        filtered_dataset = dataset.drop(dataset[dataset.city != filter_value].index)
    
    else:
        raise FilterOperationUnavailable("Filter not available for requested column", reference_column)

    grouped_dataset = group_by(filtered_dataset, reference_column)
    car_value_mean = grouped_dataset[[CAR_VALUE_COLUMN_NAME]]

    return car_value_mean