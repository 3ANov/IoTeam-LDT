Создание базы данных происходит после загрузки файлов в каталог:
- Свод по замене асфальтового покрытия-2019.xlsx
- Свод по замене асфальтового покрытия.xlsx
- odh20200928


Creat db from *.xlsx
```shell script
creat_db_from_xlsx.py
```
___
Creat TXT file from odh20200928
```shell script
creat_db_from_odh20200928.py
```
___
Creat db from odh20200928
```shell script
creat_db_geometry.py
```
___
Nested base is a demonstration option

SQL req
```sql
--Пример вывода названий обьектов которые повторяются более одного раза 
select b_2020.object_name, COUNT(*) as CNT
FROM b_2020
GROUP BY b_2020.object_name
HAVING COUNT(*) > 1;
```

```sql
--Пример вывода одинаковых полей из списка одх и титульных списков
SELECT *  FROM json, a_2019 WHERE json.name = a_2019.object_name
union
SELECT * FROM json, b_2020 WHERE json.name = b_2020.object_name;
```
