from src.controller.model.column_names import ColumnNames
import src.controller.utils.search_operations as search_operations
import src.controller.utils.read_data as read_data

def get_mean_by_city():
    dataset = read_data.openDatasets()
    response = search_operations.group_by(dataset, ColumnNames.CITY.value)
    return response.to_json()
