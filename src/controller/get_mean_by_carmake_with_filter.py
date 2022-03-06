from src.controller.model.column_names import ColumnNames
import src.controller.utils.search_operations as search_operations
import src.controller.utils.read_data as read_data

def get_mean_by_carmake_with_filter(filter):

    dataset = read_data.openDatasets()

    dataframe = search_operations.filter_by(
        dataset, ColumnNames.CAR_MAKE.value, filter)

    return dataframe.to_json()
