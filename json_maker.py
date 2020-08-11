import json as js
import data_cleaner

def iterable_to_json(my_list, keys):
    data = list()
    for item in my_list:
        values = item.split(';')
        temp_dict = {}
        for i in range(len(values)):
            temp_dict[keys[i]] = values[i]
        data.append(temp_dict)
    
    return data
        
