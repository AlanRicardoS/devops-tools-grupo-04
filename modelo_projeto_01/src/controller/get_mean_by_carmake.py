import utils.search_operations as search_operations

def get_mean_by_carmake(dataset):
    response = search_operations.group_by(dataset)
    return response
