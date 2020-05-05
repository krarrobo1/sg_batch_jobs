import pandas


excel_raw_data = pandas.read_excel('./data/dataset.xlsx', sheet_name='Hoja1', header=1)
column_names = excel_raw_data.columns
organization_idx = column_names[2:5]
values = excel_raw_data.values

# print(organization_idx)

# print("Area: ", values[1][2] + " Departamento: ", values[1][3] + " Seccion: ", values[1][4])




def getUniqueValues(list1):

    for i in range(len(values)):
        temp = values[i][2:5]
        temp.to
        print(type(temp))


getUniqueValues(values)

