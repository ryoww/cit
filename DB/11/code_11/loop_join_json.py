#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import random
import time

import json

dbname = 'cit-7.db'
# 1.�f�[�^�x�[�X�ɐڑ�
conn = sqlite3.connect(dbname)

i = 0

while i < 500:

	# 2.sqlite�𑀍삷��J�[�\���I�u�W�F�N�g���쐬
	cur = conn.cursor()
	
	#cur.execute('.mode json')
	cur.execute('select * from player inner join character on character.person_id = player.person_id;')

	#(1, 'taro', 'yamada', 0, 'D', 1, 1, 'doraemon', -267, 10, 0)
	#(1, 'taro', 'yamada', 0, 'D', 1, 2, 'akinator', -289, 5, 0)
	#(2, 'hanako', 'sato', 0, 'D', 2, 2, 'akinator', -289, 5, 0)

	list1 = []

	for row in cur:
		d = {}
		list2 = []
		
		constr = str(row[0]) + "," + str(row[1]) + "," + str(row[2])
		#print(constr) 
		
		d["player_id"] = str(row[0])
		list2.append(d)
		d["first_name"] = str(row[1])
		list2.append(d)
		d["last_name"] = str(row[2])
		list2.append(d)
		d["point"] = str(row[3])
		list2.append(d)
		d["rank"] = str(row[4])
		list2.append(d)
	
		d["character_id"] = str(row[5])
		list2.append(d)
		d["player_id"] = str(row[6])
		list2.append(d)
		d["character_name"] = str(row[7])
		list2.append(d)
		d["HP"] = str(row[7])
		list2.append(d)
		d["MP"] = str(row[8])
		list2.append(d)
		d["EXP"] = str(row[9])
		list2.append(d)
	
		list1.append(list2)
	
	print(list2)
	
	
#		for j in row:		
#			list.append(j)
	
	print(list)
	#print(type(json.dumps(list)))

	time.sleep(2)
    
# 5.�f�[�^�x�[�X�̐ڑ���ؒf
cur.close()
conn.close()
