import pandas as pd
from src.controller.utils.exceptions import FilterOperationUnavailable
from src.controller.model.column_names import ColumnNames

def group_by(dataset, group_value):
    try:
        grouped = dataset.groupby(group_value).mean()
        car_value_mean = grouped[[ColumnNames.CAR_VALUE.value]]
    except:
        raise FilterOperationUnavailable(
            "Could not group by dataset using " + group_value)

    return car_value_mean


def filter_by(dataset, reference_column, filter_value):

    filtered_dataset =_filter_dataset(dataset, reference_column, filter_value)

    grouped_dataset = group_by(filtered_dataset, reference_column)
    car_value_mean = grouped_dataset[[ColumnNames.CAR_VALUE.value]]

    return car_value_mean

def _filter_dataset(dataset, reference_column, filter_value):

    if (reference_column == ColumnNames.CAR_MAKE.value):
        return dataset.drop(dataset[dataset.car_make != filter_value].index)

    elif (reference_column == ColumnNames.CITY.value):
        return dataset.drop(dataset[dataset.city != filter_value].index)

    else:
        raise FilterOperationUnavailable(
            "Filter not available for requested column", reference_column)