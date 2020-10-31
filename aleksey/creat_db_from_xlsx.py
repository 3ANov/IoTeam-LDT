#  https://t.me/elemnt3 Y:2020

import sqlite3 as sq
import pandas as pd
import os

PATH_DB = os.path.dirname(os.path.join(os.getcwd(), 'data.db/'))


def creat_db():
    """Creating tables in the database from <name>.xlsx """
    pd_read_2019 = pd.read_excel('Свод по замене асфальтового покрытия-2019.xlsx',
                                 sheet_name='Корректировка на 06.09',
                                 usecols='A:K',
                                 header=6,
                                 nrows=871
                                 )
    pd_read_2020 = pd.read_excel('Свод по замене асфальтового покрытия.xlsx',
                                 sheet_name='общий  ',
                                 usecols='A:K',
                                 header=4,
                                 nrows=1153
                                 )

    # размер (1153, 12) строка/столбцы 2020
    # data_pd.columns - Выводит названия столбцов в таблице
    # pd_read_2019.columns = ['№', 'object_name', 'repair_border_start', 'repair_border_stop', 'county', 'basis_for_inclusion','program', 'object_category', 'carriageway', 'carriageway', 'sidewalks', 'roadside']
    # pd_read_2019.columns = ['№', 'Наименование объекта', 'Границы начальная', 'Границы конечная', 'Округ', 'Основание для включения','Программа', 'Категория объекта', 'Проезжая часть', 'Проезжая часть', 'Тротуары', 'Обочины']

    pd_read_2019.rename({1: 'id', 2: 'object_name', 3: 'repair_border_start', 4: 'repair_border_stop', 5: 'county',
                         6: 'basis_for_inclusion', 7: 'program', 8: 'object_category', 9: 'carriageway',
                         10: 'sidewalks', 11: 'roadside'}, axis=1,
                        inplace=True)

    pd_read_2020.rename({1: 'id', 2: 'object_name', 3: 'repair_border_start', 4: 'repair_border_stop', 5: 'county',
                         6: 'basis_for_inclusion', 7: 'program', 8: 'object_category', 9: 'carriageway',
                         10: 'sidewalks', 11: 'roadside'}, axis=1,
                        inplace=True)
    with sq.connect(PATH_DB) as connection:
        try:

            pd_read_2019.to_sql('2019', connection, if_exists='replace',
                                index=False)
        except sq.Error as error:
            print('"Failed creat table", error')

    with sq.connect(PATH_DB) as connection:
        try:

            pd_read_2019.to_sql('2020', connection, if_exists='replace',
                                index=False)
        except sq.Error as error:
            print('"Failed creat table", error')


# Try me ^)
if __name__ == '__main__':
    creat_db()
