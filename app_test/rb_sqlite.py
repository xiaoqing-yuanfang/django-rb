# -*- coding:utf-8 -*-
import os
import time

from app_test.lib import get_rb_data
from app_test.lib import sqlite3_op


def init_database(default_dbname="rb.sqlite3"):
    flag = sqlite3_op.create_table_rb("rb")
    if(flag == False):
        print("create tabel failed")
        exit(1)
    data = []
    for i in range(2003,2015,1):
        import time;time.sleep(1)
        tmp = get_rb_data.search_rb_items(i)
        if(tmp != None):
            tmp = get_rb_data.search_rb_item(tmp)
            if(tmp != None):
                tmp.reverse()
                data += tmp
    for i in data:
        sqlite3_op.insert_into_table_rb("rb",i) 
    os.system("cp rb.sqlite3 rb.sqlite3.backup")    
def newest_phase_in_database(database_name="rb.sqlite3",table_name="rb"):
    import sqlite3
    import os
    flag = os.path.exists(database_name)
    if(flag == False):
        print("sqlite3 database doesn't exist")
        os.sys.exit() 
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()
    result_cur = cur.execute(
            '''select max(qishu) from %s''' %table_name
            )
    result = result_cur.fetchone()
    return int(result[0]) 
def update_database(database_name="rb.sqlite3"):
    cur_year = int(time.asctime().split()[4])        
    newest_in_database = newest_phase_in_database()
    tmp = get_rb_data.search_rb_items(cur_year)
    if(tmp != None):
        tmp = get_rb_data.search_rb_item(tmp)
    to_add = []
    for i in tmp:
        if(int(i[1]) > newest_in_database):
            to_add.append(i)
    to_add.reverse()
    for i in to_add:
        sqlite3_op.insert_into_table_rb("rb",i) 
        print("sync %s " %i)
    print("sync completed")