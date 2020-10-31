#  https://t.me/elemnt3 Y:2020

import json
import os
import sqlite3 as sq

PATH_DB = os.path.dirname(os.path.join(os.getcwd(), 'data.db/'))

with sq.connect(PATH_DB) as con:
    cur = con.cursor()
    cur.execute("""
    DROP TABLE IF EXISTS json
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS json(
    id INTEGER PRIMARY KEY,
    root_id INTEGER,
    distance REAL,
    object_id INTEGER,
    name TEXT,
    geometry TEXT,
    geometry_type TEXT,
    coordinates TEXT
    )
    """)
    try:
        sqlite_insert_with_param = """INSERT INTO json
                          (id, root_id, distance, object_id, name, geometry, geometry_type,coordinates)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
        with open('odh20200928', 'r', encoding='utf-8') as f:
            lines = f.read().split('\n')
            for i in range((len(lines)) - 1):
                if 'name' in lines[i]:
                    id = i + 1
                    name = json.loads(lines[i])['name']
                    root_id = json.loads(lines[i])['root_id']
                    object_id = json.loads(lines[i])['object_id']
                    distance = json.loads(lines[i])['distance']
                if 'geometry' in lines[i]:
                    geometry = str(json.loads(lines[i])['geometry'])  # all data
                    if json.loads(lines[i])['geometry']['type'] == 'GeometryCollection':
                        geometry_type = str(json.loads(lines[i])['geometry']['geometries'][1]['type'])
                        coordinates = str(json.loads(lines[i])['geometry']['geometries'][1]['coordinates'])
                        print(geometry_type)
                        print(coordinates)
                    elif json.loads(lines[i])['geometry']['type'] != 'GeometryCollection':
                        geometry_type = str(json.loads(lines[i])['geometry']['type'])
                        coordinates = str(json.loads(lines[i])['geometry']['coordinates'])

                if 'geometry' not in lines[i]:
                    geometry = 0
                data_tuple = (id, root_id, distance, object_id, name, geometry, geometry_type, coordinates)
                cur.execute(sqlite_insert_with_param, data_tuple)
                con.commit()
                print("Inserted successfully")
                con.cursor()
    except sq.Error as error:
        print("Failed to insert", error)
    finally:
        print("Closed")
