import src.controller.utils.search_operations as search_operations
import src.controller.utils.read_data as read_data

CITY_COLUMN_NAME = 'city'


def get_mean_by_city_with_filter(filter):

    dataset = read_data.openDatasets()

    dataframe = search_operations.filter_by(
        dataset, CITY_COLUMN_NAME, filter)

    return dataframe.to_json()
