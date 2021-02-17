import sqlite3
test=sqlite3.connect('test.db')
'''cursor=test.cursor()
cursor.execute('create table LendInfo (id int,isbn varchar(20) primary key,lenddate datetime,returndate datetime,renev bit)')
cursor.execute('insert into LendInfo values (10012101,\'978-7-302-23817-1\',2012-07-05,2012-09-05,\'faslse\')')
print(cursor.rowcount)
cursor.close()
test.commit()
test.close()'''
cursor=test.cursor()
"""cursor.execute('insert into LendInfo values (10012102,\'978-7-302-23817-2\',\'20120705\',\'2012-09-05\',\'faslse\')')"""
"""cursor.execute('select * from LendInfo where id=?', ('10012102',))"""
cursor.execute('select * from LendInfo')
values = cursor.fetchall()
print(values)
cursor.close()
test.commit()

