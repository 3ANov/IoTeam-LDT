import json

from file_processing.models import FileModel
from map.models import OdhRecord


def parsing_odh_file():
    if FileModel.objects.filter(content_type='ODH_DATA').first() is not None:
        f = FileModel.objects.filter(content_type='ODH_DATA').first()
        lines = f.content.open('r').read().split('\n')
        for i in range((len(lines)) - 1):
            if 'name' in lines[i]:
                name = json.loads(lines[i])['name']
                root_id = json.loads(lines[i])['root_id']
                object_id = json.loads(lines[i])['object_id']
                distance = json.loads(lines[i])['distance']
            if 'geometry' in lines[i]:
                geometry = str(json.loads(lines[i])['geometry'])  # all data
                if json.loads(lines[i])['geometry']['type'] == 'GeometryCollection':
                    geometry_type = str(json.loads(lines[i])['geometry']['geometries'][1]['type'])
                    coordinates = str(json.loads(lines[i])['geometry']['geometries'][1]['coordinates'])
                elif json.loads(lines[i])['geometry']['type'] != 'GeometryCollection':
                    geometry_type = str(json.loads(lines[i])['geometry']['type'])
                    coordinates = str(json.loads(lines[i])['geometry']['coordinates'])

            if 'geometry' not in lines[i]:
                geometry = 0
            OdhRecord.objects.create(root_id=root_id,
                                     distance=distance,
                                     object_id=object_id,
                                     name=name,
                                     geometry=geometry,
                                     geometry_type=geometry_type,
                                     coordinates=coordinates)
