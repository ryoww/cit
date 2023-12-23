#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import time

dbname = 'cit-db-2023-10.db'
conn = sqlite3.connect(dbname)

cur = conn.cursor()

start = time.time() 
cur.execute('SELECT E.ts, C.character_name FROM event E INNER JOIN character C ON E.character_id_dst == C.character_id WHERE E.action_type == \'attack\'');


dict_list = []

counter = 0
for row in cur:
    #print(row[1])
    dict_list.append(row[1])
    counter = counter + 1

print(counter)

import collections
c = collections.Counter(dict_list)

print(c)

cur.close()
conn.close()