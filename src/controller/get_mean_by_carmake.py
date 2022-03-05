import src.controller.utils.search_operations as search_operations
import src.controller.utils.read_data as read_data

CAR_MAKE_COLUMN_NAME = 'car_make'


def get_mean_by_carmake():
    dataset = read_data.openDatasets()
    response = search_operations.group_by(dataset, CAR_MAKE_COLUMN_NAME)
    return response.to_json()
