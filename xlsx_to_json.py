import pandas as pd
import data_cleaner as dc
import json_maker as jm
import json

def join_data(arr): 
    return ";".join(str(v) for v in arr)

def get_relations(values, start, end):
    relation = set()
    for value in values:
        rows = value[start:end]
        relation.add(join_data(rows))
    return relation

def set_labels_ids(values, idx):
    labels_ids = set()
    for value in values:
        rows = value[idx]
        # Normalize labels, remove accents and whitespaces
        label = dc.normalize(str(rows))
        # Make an identifier
        id = dc.id_maker(str(rows))
        # Concat label and id
        label_id = label+";"+id
        # Add value to set to get unique values
        labels_ids.add(label_id)

    return labels_ids

def set_reference(relation, ref, field, collection):
    for rel in relation:
        referrals = rel.split(';')
        print(referrals)
        for r in ref:
            if(dc.normalize(referrals[1]) == r['label']):
                r[field] = {'name': dc.normalize(referrals[0]), 'reference': collection+'/'+dc.id_maker(referrals[0]) }
                

def main():
    # Read dataset
    df = pd.read_excel('./data/dataset.xlsx', sheet_name='Hoja1', header=1)
    values = df.values

    # Get unique values
    areas = set_labels_ids(values, 2)
    # Transform to dictionary
    area_list = jm.iterable_to_json(areas, ['label', 'id'])
    # Write Areas json
    with open('./data/areas.json', 'w') as fp:
        json.dump(area_list, fp)

    # Get area and department column relations
    area_dept_rel = get_relations(values, 2,4)   # Relacion areas - departamentos
    # Set label and id's
    departments = set_labels_ids(values, 3)
    dpt_list = jm.iterable_to_json(departments, ['label', 'id'])
    # Set reference object to json
    set_reference(area_dept_rel, dpt_list, 'area', 'academic-areas')
    #Write json file
    with open('./data/departments.json', 'w') as fp:
        json.dump(dpt_list, fp)

    # Get department - section column relations
    dept_sect_rel = get_relations(values, 3,5)
    sections = set_labels_ids(values, 4)
    # Set label and id's
    section_list = jm.iterable_to_json(sections, ['label', 'id'])
    # Set reference object to json
    set_reference(dept_sect_rel, section_list, 'department', 'departments')

    #Write json file
    with open('./data/sections.json', 'w') as fp:
        json.dump(section_list, fp)
    

if __name__ == '__main__':
    main()
    