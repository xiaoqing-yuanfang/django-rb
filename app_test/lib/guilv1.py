import sqlite3
from app_test.lib import search 
from app_test.lib import sqlite3_op
import os
import math
debug = False
def guilv1_red_create_table(table_name="guilv1_red",lianxu_n = 2):
    ''' 
        succ return True
        failed return False
    '''    
    try:
        flag = os.path.exists("rb.sqlite3")
        if(flag == False):
            print("database rb.sqlite3 doesn't exists")
        else:
            pass 
        cols = "" 
        for i in range(1,34):
            if(i != 33):
                cols += "rate_%s float," %i
            else:
                cols += "rate_%s float" %i
        conn = sqlite3.connect("rb.sqlite3")
        cur = conn.cursor()
        cur.execute(
                    '''create table %s(id int primary key,lianxu_n int ,%s
                                        )''' %(table_name,cols)
                    ) 
        conn.commit()
        return True
    except sqlite3.OperationalError as e:
        print("sqlite3.OperationalError\t" + str(e))
        return False
def guilv1_get_red_rate_lianxu_n(items,lianxu_n=2):
    '''
    items should be six tuple
    return [[id,lianxu_n,rate_1,rate_2,rate_3,..., rate_33]]
    '''
    if(len(items) < lianxu_n):
        print("items is too short to compute")
        exit(1)
    results = []
    id = 1
    fenmu = lianxu_n *6
    reds = []
    for i in range(1,34):
       reds.append(i) 
    
    for i in range(len(items)):
        if(i == (len(items) - lianxu_n+1)):
            break
        fenzi = [0]*33
        result = []
        result.append(id)
        result.append(lianxu_n)
        data = []
        cur_item = i
        for j in range(lianxu_n):
            data += items[cur_item] 
            cur_item += 1
        for j in data:
            j = int(j)
            fenzi[j-1] += 1
        for j in range(33):
            #result.append(fenzi[j]/fenmu)
            result.append(fenzi[j])
        results.append(result) 
        id += 1
    return results
def guilv1_store_rate_red_to_database(table_name="test",items=None):
    if(items == None or table_name == None):
        exit(1)
    flag = os.path.exists("rb.sqlite3")
    if(flag == False):
        print("sqlite3 database doesn't exist")
        os.sys.exit()
        
    conn = sqlite3.connect("rb.sqlite3")
    cur = conn.cursor() 
    # insert 
    for line in items:
        cur.execute(
                    '''insert into %s values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''' %table_name,line
                    )
    conn.commit()    
def guilv1_red_init(items,file_name = None,table_name="guilv1_red",lianxu_n = 2):
    '''
    items should 6 elements red balls
    file_name is the file to store the result
    table_name is the table name in database "rb.sqlite3" which stores the result
    return True or False
    note: this function will take few minutes,so when call it when necessary.
    '''    
    flag = False
    t = table_name
    for i in range(lianxu_n,lianxu_n+1,1):
        table_name = t + "_" + str(i)
        try:
            flag = sqlite3_op.drop_table(table_name) 
        except sqlite3.OperationalError as e:
            print("warning",e)
            pass
        flag = guilv1_red_create_table(table_name=table_name,lianxu_n=i)
        if(flag == True):
            rates = guilv1_get_red_rate_lianxu_n(items=items,lianxu_n=i)    
            guilv1_store_rate_red_to_database(table_name=table_name,items=rates)
        else:
            print("table guilv1_red table create failed")
            exit(1)
    
def guilv1_red_update(items,file_name = None,table_name="guilv1_red"):
    '''
    items should 6 elements red balls
    file_name is the file to store the result
    table_name is the table name in database "rb.sqlite3" which stores the result
    return the result 
    '''    
    
def guilv1_blue_init(items,file_name = None,table_name="guilv1_blue",lianxu_n=2):
    '''
    items should be list
    store rate of 16 blue numbers to database and return it
    return nums/periods
    '''
    d = dict()
    for i in range(1,17):
        d[i] = 0
    for i in blues:
        d[i] += 1
    d['num'] = len(items)
    return d


def guilv1_blue_update(items,file_name = None,table_name="guilv1_blue"):
    pass    
class guilv1_stat(object):
    def __init__(self,database_name="rb.sqlite3",table_name_prefix="guilv1_red_"):
        self.database_name = database_name
        self.table_name_prefix = table_name_prefix
        
        flag = os.path.exists("rb.sqlite3")
        if(flag == False):
            print("sqlite3 database doesn't exist")
            os.sys.exit()
            
        self.conn = sqlite3.connect("rb.sqlite3")
        self.cur = self.conn.cursor() 
       # # insert 
       # for line in items:
       #     cur.execute(
       #                 '''insert into %s values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''' %table_name,line
       #                 )
       # conn.commit()    
    def get_avg_rate_red(self,red_ball=1,lianxu_n=2):
        '''
            return average rate of red ball in lianxu_n periods
        '''
        table_name = self.table_name_prefix + str(lianxu_n)
        str_sql = "select avg(rate_%s) from %s" %(red_ball,table_name)
        self.cur.execute(str_sql)
        cur_result = self.cur.fetchall()
        for i  in cur_result:
            pass
            #print(i)
        return i[0]/lianxu_n
    def get_min_max_rate_red(self,red_ball=1,lianxu_n=2):
        '''
            return (min,max) tuple
        '''
        table_name = self.table_name_prefix + str(lianxu_n)
        str_sql = "select min(rate_%s),max(rate_%s) from %s" %(red_ball,red_ball,table_name)
        self.cur.execute(str_sql)
        cur_result = self.cur.fetchall()
        #for i  in cur_result:
            #print(i)
        return cur_result[0]
    def __exit__():
        self.conn.close()
def get_redballs_comply_stat_min_max(lianxu_n=2):
    '''
        return red numbers comply with min < redball_number < max
    '''
    stat_guilv1 =  guilv1_stat()
    
    d = dict()
    for i in range(1,34):
        d[i] = stat_guilv1.get_min_max_rate_red(red_ball=i,lianxu_n=lianxu_n)

    ##
    # get top lianxu_n-1 items form database
    ##
    ###
    #p_from,p_to,p_len = search.from_and_to(table_name="rb")
    #all_items = search.search_3(periods_from=p_from,periods_to=p_to,table_name="rb")
    #top_lianxu_n_reds = search.get_red_2(buf=all_items)
    #rate  = guilv1_get_red_rate_lianxu_n(top_lianxu_n_reds[:lianxu_n-1],lianxu_n=lianxu_n-1)
    rate = search.get_redrate_lianxu_n_id(lianxun=lianxu_n-1,id=1)
    if(len(rate) != 1):
        print("result get error")
        exit(1)
    rate = rate[0]
    rate = list(rate)
    for i in range(1):
        rate.pop(0)
    r = []
    for i in range(1,34):
        if(debug==True):
            print(i,":",rate[i],d[i][0],d[i][1])
        if((rate[i]+1) >= d[i][0] and rate[i]+1 <= d[i][1]):
            r.append(i)
    return r

if __name__ == "__main__":
    import os
    import shutil
    
    p_from,p_to,p_len = search.from_and_to(table_name="rb")
    all_items = search.search_3(periods_from=p_from,periods_to=p_to,table_name="rb") 
    blues = search.get_blue_2(buf=all_items)
    rates = guilv1_blue_init(blues)    
    blues = blues[:100]