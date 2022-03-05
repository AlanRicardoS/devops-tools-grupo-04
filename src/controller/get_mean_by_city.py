import src.controller.utils.search_operations as search_operations
import src.controller.utils.read_data as read_data

CITY_COLUMN_NAME = 'city'


def get_mean_by_city():
    dataset = read_data.openDatasets()
    response = search_operations.group_by(dataset, CITY_COLUMN_NAME)
    return response.to_json()
