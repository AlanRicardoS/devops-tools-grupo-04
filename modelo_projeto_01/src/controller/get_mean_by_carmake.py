import src.controller.utils.search_operations as search_operations

def get_mean_by_carmake():
    response = search_operations.group_by()
    return response.to_json()
