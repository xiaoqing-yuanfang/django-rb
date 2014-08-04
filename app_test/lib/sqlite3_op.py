
import sqlite3
import os
from app_test.lib import search
from app_test.lib import predict

def insert_next_period_item_rb_red_predict_version(table_name = "rb",six_list=[]):
    '''
       six_list is a must arg
       this function can use when guilv1
    '''
    assert(len(six_list)==6)
    ## here assums rb_temp is a backuptable of table_name "rb"
    start,end,length = search.from_and_to(table_name="rb_temp")
    next_item = start +1
    six_list.insert(0,next_item) ## qishu
    six_list.insert(0,0)         ## date
    six_list.append(0)           ## blue number
    delete_from_table_rb(table_name,qishu=next_item)
    insert_into_table_rb(table_name,tuple(six_list))

    
    

def copy_table_items(table_name1,table_name2):
    '''
    table_name2 is the target table
    this function equals to create the table_name2 and copy data from table_name1 to table_name2
    no matter table_name2 exists.
    attention,table table_name2 should have exists;
    succ return True;
    failed return False;
    '''
    
    flag = os.path.exists("rb.sqlite3")
    if(flag == False):
        print("sqlite3 database doesn't exist")
        os.sys.exit()
        
    conn = sqlite3.connect("rb.sqlite3")
    cur = conn.cursor()
    if(if_exists_table(table_name1) == False):
        print("table ",table_name1,"doesn't exists")
        return False
    if(if_exists_table(table_name2) == False):
        create_table_rb(table_name2)
    else:
        cur.execute(
            '''delete from  %s''' %(table_name2)
                    )
        ### commit could make action execute right now,otherwise
        conn.commit()
    items_to_insert = search.search_3(table_name=table_name1)
    cur.executemany('''insert into %s values(?,?,?,?,?,?,?,?,?)''' %table_name2,items_to_insert)
    conn.commit()
    return True
    
def if_exists_table(table_name):
    ''' 
        succ return True
        failed return False
    '''    
    try:
        flag = os.path.exists("rb.sqlite3")
        if(flag == False):
            print("sqlite3 database doesn't exist")
            os.sys.exit()
            
        conn = sqlite3.connect("rb.sqlite3")
        cur = conn.cursor()
        cur.execute( '''select * from %s '''  %(table_name))
        conn.commit()
        return True
    except sqlite3.OperationalError as e:
        print("sqlite3.OperationalError\t" + str(e))
        return False
        
def create_table_rb(table_name):
    ''' 
        succ return True
        failed return False
    '''    
    try:
        flag = os.path.exists("rb.sqlite3")
        if(flag == False):
            os.system("touch rb.sqlite3")
        else:
            os.system("cp rb.sqlite3 rb.sqlite3.backup")
            os.system("rm -f rb.sqlite3")
            
        conn = sqlite3.connect("rb.sqlite3")
        cur = conn.cursor()
        cur.execute(
                    '''create table %s(date text, 
                                        qishu int,
                                        r1 int,
                                        r2 int,
                                        r3 int,
                                        r4 int,
                                        r5 int,
                                        r6 int,
                                        b1 int
                                        )''' %(table_name)
                    ) 
        conn.commit()
        return True
    except sqlite3.OperationalError as e:
        print("sqlite3.OperationalError\t" + str(e))
        return False

def drop_table(table_name):
    ''' 
        succ return True
        failed return False
    '''
    try:
        flag = os.path.exists("rb.sqlite3")
        if(flag == False):
            print("sqlite3 database doesn't exist")
            os.sys.exit()
            
        conn = sqlite3.connect("rb.sqlite3")
        cur = conn.cursor()
        cur.execute(
                    '''drop table %s''' %(table_name)
                    )
        conn.commit()
        return True
    except sqlite3.OperationalError as e:
        print("sqlite3.OperationalError\t"+str(e))
        return False
def delete_from_table_rb(table_name="rb",qishu=None):
    ##################
    #### if qishhu == None ,delete the largetst qishu
    ##################
    if(qishu == None):
        pass
    flag = os.path.exists("rb.sqlite3")
    if(flag == False):
        print("sqlite3 database doesn't exist")
        os.sys.exit()
        
    conn = sqlite3.connect("rb.sqlite3")
    cur = conn.cursor() 
    if(qishu == None):
        start,end,length = search.from_and_to(table_name=table_name)
        qishu = start
    cur.execute(
                '''delete from %s where qishu = %s''' %(table_name,qishu)
                )
    conn.commit()
    
def insert_into_table_rb(table_name,row):
    ##################
    #### rows should be 9 tuple
    ##################
    flag = os.path.exists("rb.sqlite3")
    if(flag == False):
        print("sqlite3 database doesn't exist")
        os.sys.exit()
        
    conn = sqlite3.connect("rb.sqlite3")
    cur = conn.cursor() 
    line = row
    # insert 
    cur.execute(
                '''insert into %s values(?,?,?,?,?,?,?,?,?)''' %table_name,line
                )
    conn.commit()

#flag = os.path.exists("rb.sqlite3")
#if(flag == False):
#    print("sqlite3 database doesn't exist")
#    os.sys.exit()
#    
#conn = sqlite3.connect("rb.sqlite3")
#cur = conn.cursor()

# create table rb
#cur.execute(
#            '''create table rb(date text, 
#                                qishu int,
#                                r1 int,
#                                r2 int,
#                                r3 int,
#                                r4 int,
#                                r5 int,
#                                r6 int,
#                                b1 int
#                                )'''
#            )


## insert 
#cur.execute(
#            '''insert into rb values("2013-01-01",201314,1,2,3,4,5,6,7)'''
#            )


##  delete
#cur.execute(
#            '''delete from rb where r1=1 '''
#            )


## select 
#buf_select = cur.execute(
#            '''select * from rb '''
#            )
#
#for i in buf_select:
#    print(i)
#
#while(True):
#    
#    if(int(input("do you wnat to insert new items 1 yes/ 0 no:")) == 0): break
#    a0,a1,a2,a3,a4,a5,a6,a7,a8 = input("format:2013-01-01 201314 1 2 3 4 5 6 7\n").split()
#    line = (a0,a1,a2,a3,a4,a5,a6,a7,a8)
#    # insert 
#    cur.execute(
#                '''insert into rb values(?,?,?,?,?,?,?,?,?)''',line
#                )
#    conn.commit()
#
#
## select 
#buf_select = cur.execute(
#            '''select * from rb '''
#            )
#
#for i in buf_select:
#    print(i)
#import pdb;pdb.set_trace()


#s = "abc"
#ss = s.zfill(5)
#print(ss)

#create table temp
#cur.execute(
#            '''create table temp(num text, 
#                                hit_cishu text,
#                                num_a_cycle text,
#                                rates_of_num text
#                                )'''
#            )
#conn.close()
def fenxi_cycle_from_sqlite():
     # here use the temp table in sqlite3 named "temp" which the author named it
    import sqlite3
    import os
    flag = os.path.exists("rb.sqlite3")
    if(flag == False):
        print("sqlite3 database doesn't exist")
        os.sys.exit()
        
    conn = sqlite3.connect("rb.sqlite3")
    cur = conn.cursor()
    
    result_cur = cur.execute(
                '''select hit_cishu,count(hit_cishu) from temp group by(hit_cishu)'''
                )
    tmp = []
    
    for i in result_cur:
        tmp.append(i)
    del result_cur

    result_cur = cur.execute(
            '''select max(hit_cishu) from temp'''
            )
    i = int(cur.fetchall()[0][0])
    #print(i)
    tmp.append("-----------------------------")
    for i in range(0,6):
        j = (str(i).rjust(3).replace(' ','0'),)
        result_cur = cur.execute('''select num,hit_cishu from temp where hit_cishu=(?)''',j)
        for r in result_cur:
            tmp.append(r)
        tmp.append('--------------------------------')
    #print(tmp)
    
    conn.close()
    
    return tmp

def integrity_check_table_rb():
    import sqlite3
    import os
    flag = os.path.exists("rb.sqlite3")
    if(flag == False):
        print("sqlite3 database doesn't exist")
        os.sys.exit()
        
    conn = sqlite3.connect("rb.sqlite3")
    cur = conn.cursor()    
    result_cur = cur.execute(
                '''select  count(qishu) from (select distinct * from rb)'''
                )
    count_distinct = int(result_cur.fetchone()[0])
    
    result_cur = cur.execute(
                '''select  count(qishu) from (select  * from rb)'''
                )
    count_all = int(result_cur.fetchone()[0])
    
    result_cur = cur.execute(
                '''select max(qishu) from rb'''
                )
    max =   int(result_cur.fetchone()[0])
    
    result_cur = cur.execute(
                '''select min(qishu) from rb'''
                )
    min =   int(result_cur.fetchone()[0])
    if(max-min+1 != count_distinct):
        print(count,max,min)
        print("table rb error checked!!!")
        os.sys.exit()
        return False
    if(count_all > count_distinct):
        print("there are repeated item in database")
        return False
    return True
if(__name__ == "__main__"):
    copy_table_items("rb_temp","rb")
    