import pandas

# Data cleaning functions
import data_cleaner
# Json functions
import json_maker

# Reads xlsx File
excel_raw_data = pandas.read_excel('./data/dataset.xlsx', sheet_name='Hoja1', header=1)
# Get colum_names
column_names = excel_raw_data.columns
# Organization Fields: Areas, Departamento, Seccion
organization_idx = column_names[2:5]
values = excel_raw_data.values

# Create a set for each Organization field
depts = set()
areas = set()
sections = set()

for value in values:
    temp = value[2:5]
    for i in range(len(temp)):
        if type(temp[i]) != float:
            value = data_cleaner.normalize(temp[i])
            if i == 0:
                areas.add(value)
            elif i == 1:
                depts.add(value)
            else:
                sections.add(value)

depts_data = json_maker.list_to_json(list(depts))
json_maker.write_json(depts_data, './data/depts_data.json');

