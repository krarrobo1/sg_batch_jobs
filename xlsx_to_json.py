import pandas as pd
import data_cleaner as dc

def join_data(arr): 
    return ";".join(str(v) for v in arr)

def get_relations(values, start, end):
    relation = set()
    for value in values:
        rows = value[start:end]
        relation.add(join_data(rows))
    return relation

def get_labels_and_ids(values, idx):
    labels_ids = set()
    for value in values:
        rows = value[idx]
        label = str(rows).strip()
        id = dc.id_maker(str(rows))
        label_id = "label:"+label+","+"id:"+id
        labels_ids.add(label_id)

    return labels_ids

def main():
    df= pd.read_excel('./data/dataset.xlsx', sheet_name='Hoja1', header=1)
    # # Relacion areas - departamentos
    # area_dept_rel = get_relations(df.values, 2,4)
    # # Relacion departamentos - secciones
    # dept_sect_rel = get_relations(df.values, 3,5)

    # print(area_dept_rel)
    # print("")
    # print(dept_sect_rel)
    print('Areas \n')
    print(get_labels_and_ids(df.values, 2))
    print('Departments \n')
    print(get_labels_and_ids(df.values, 3))
    print('Sections \n')
    print(get_labels_and_ids(df.values, 4))


if __name__ == '__main__':
    main()
    