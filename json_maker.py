import json
import data_cleaner

def list_to_json(my_list):
    dictionaries = list()
    for item in my_list:
        id = data_cleaner.id_maker(item)
        dictionaries.append({ 'id': id , 'label': item })

    return dictionaries


def write_json(data, directory):
    with open(directory, 'w') as fp:
        json.dump(data, fp)
