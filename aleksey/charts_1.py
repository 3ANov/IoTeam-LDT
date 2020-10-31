#  https://t.me/elemnt3 Y:2020

import sqlite3 as sq

# For charts_1.html
with sq.connect('data.db') as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.execute("""
    select COUNT(DISTINCT a_2019.object_name) from a_2019;
    """)
    count_dictinct_2019 = cur.fetchone()[0]  # 843 uni
    cur.execute("""
    select COUNT(a_2019.object_name) from a_2019;
    """)
    count_2019 = cur.fetchone()[0]  # 871 Not uni
    cur.execute("""
    select COUNT(DISTINCT b_2020.object_name) from b_2020;
    """)
    count_dictinct_2020 = cur.fetchone()[0]  # 1134 uni
    cur.execute("""
    select COUNT(b_2020.object_name) from b_2020;
    """)
    count_2020 = cur.fetchone()[0]  # 1153 Not uni
count = [count_dictinct_2019, count_dictinct_2020, count_2019, count_2020]

