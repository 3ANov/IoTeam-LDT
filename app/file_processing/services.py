#  https://t.me/elemnt3 Y:2020

import json

# creat example for TXT FORMAT FILES file and correct quickly
# creat
from file_processing.models import FileModel

print(FileModel.objects.get(content_type='ODX_DATA'))
with open('odh20200928', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
js = json.loads(lines[0])
with open('data_from_json.txt', 'w', encoding='utf-8') as f:
    """Name, Passport_draft_org, Geometry"""
    print('Count:', len(lines), file=f)
    try:
        for i in range((len(lines)) - 1):
            print('Name: ', (json.loads(lines[i])['name']), file=f)
            if 'passport_draft_org' in lines[i]:
                print('Passport_draft_org:', (json.loads(lines[i])['passport_draft_org']),
                      file=f)
            if 'geometry' in lines[i]:
                print('Geometry', (json.loads(lines[i])['geometry']), file=f)
            print('===========================================================================', file=f)
    except IndexError as err:
        print(err)
# ALL 7596
# 19
tags = ["name", "tree", "root_id", "distance", "end_date", "geometry", "owner_id", "file_list", "object_id",
        "start_date", "customer_id", "department_id", "passport_date", "calc_attribute", "declare_length",
        "is_orphan_object", "clean_category_id", "ogh_object_type_id", "passport_draft_org"]
# 23
all_tags = ['name',
            'tree',
            'root_id',
            'distance',
            'end_date',
            'geometry',
            'owner_id',
            'file_list',
            'object_id',
            'snow_area',
            'rotor_area',
            'start_date',
            'axis_length',
            'customer_id',
            'reagent_area',
            'department_id',
            'layout_length',
            'passport_date',
            'calc_attribute',
            'is_orphan_object',
            'clean_category_id',
            'ogh_object_type_id',
            'passport_draft_org']
