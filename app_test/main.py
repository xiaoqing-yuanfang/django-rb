# -*- coding:utf-8 -*-
import os
import sys

new_lib = os.path.join(os.path.dirname("__file__"), "../")
sys.path.append(new_lib)
print(sys.path)

from app_test.lib import guilv1
from app_test.lib import search
from app_test.lib import sqlite3_op
from app_test import rb_sqlite
if(__name__ == "__main__"):
    #rb_sqlite.init_database()
    rb_sqlite.update_database()    
    #p_from,p_to,p_len = search.from_and_to(table_name="rb")
    #all_items = search.search_3(periods_from=p_from,periods_to=p_to,table_name="rb") 
    #reds = search.get_red_2(buf=all_items)            
    #guilv1.guilv1_red_init(reds,lianxu_n=p_len)
    p_from,p_to,p_len = search.from_and_to(table_name="rb")
    all_items = search.search_3(periods_from=p_from,periods_to=p_to,table_name="rb") 
    reds = search.get_red_2(buf=all_items)
    for i in range(1569,p_len+1):
        guilv1.guilv1_red_init(reds,lianxu_n=i)
    for i in range(p_len,p_len-1,-1): 
        guilv1_stat = guilv1.guilv1_stat() 
        r_lianxu_n = guilv1.get_redballs_comply_stat_min_max(lianxu_n=1000)
        print(r_lianxu_n)
    ## 验证  
    sqlite3_op.delete_from_table_rb(qishu=p_from)
    sqlite3_op.delete_from_table_rb(qishu=p_from-1)
    p_from,p_to,p_len = search.from_and_to(table_name="rb")
    for i in range(p_len,p_len-1,-1): 
        guilv1_stat = guilv1.guilv1_stat()   
        r_lianxu_n = guilv1.get_redballs_comply_stat_min_max(lianxu_n=1001)
        print(r_lianxu_n)
        
    ## 验证完恢复数据库
    ##rb_sqlite.update_database()    
