# テストデータ(JSON, CSV)の生成1
<pre>
dummyjson sample-json.hbs > test_data.json
dummyjson sample-csv.hbs > test_data.csv
</pre>

# CSVファイルのsqliteへの取り込み
<pre>
Use ".open FILENAME" to reopen on a persistent database.
sqlite> .mode csv

sqlite> .import test_data.csv test_data
test_data.csv:2: expected 8 columns but found 7 - filling the rest with NULL

sqlite> .tables
test_data

sqlite> select * from test_data where id=48;
48,"Francis Winter",Xenosys,1989,"65 Elton Way",Medford,false,
</pre>

# テストデータ(JSON, CSV)の生成2
<pre>
https://json-generator.com/
</pre>

<pre>
保存したJSONファイルをCSVに変換(Linux)
# in2csv person.json  > person.csv
/usr/lib/python3.6/importlib/_bootstrap.py:219: ImportWarning: can't resolve package from __spec__ or __package__, falling back on __name__ and __path__
</pre>