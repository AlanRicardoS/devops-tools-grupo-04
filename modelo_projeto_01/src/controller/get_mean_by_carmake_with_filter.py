import src.controller.utils.search_operations as search_operations
import src.controller.utils.read_data as read_data

CAR_MAKE_COLUMN_NAME = 'car_make'

def get_mean_by_carmake_with_filter(filter):

    dataset = read_data.openDatasets()

    dataframe = search_operations.filter_by(dataset, CAR_MAKE_COLUMN_NAME, filter)

    return dataframe.to_json()
