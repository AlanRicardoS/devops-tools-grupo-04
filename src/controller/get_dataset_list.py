import src.controller.utils.read_data as read_data


def get_dataset_list():
    dataset = read_data.listOfDatasets()

    jsonArray = []

    count = 0

    for i in range(0, len(dataset)):
        response = {"id": count + 1, "dataset": dataset[i]}
        print(response)
        count += 1
        jsonArray.append(response)

    return jsonArray
