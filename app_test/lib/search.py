import sqlite3
import os
from app_test.lib import tools

def from_and_to(table_name="rb"):
    ''' 
    this function takes no arg and 
    return tuple (period_from,period_to,list_len) to caller
    '''

    flag = os.path.exists("rb.sqlite3")
    if(flag == False):
        print("sqlite3 database doesn't exist")
        os.sys.exit()
        
    conn = sqlite3.connect("rb.sqlite3")
#   conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    
    
    # select 

    cur.execute(
                '''select  * from %s order by qishu desc''' %table_name
                )
    
    list_result = cur.fetchall()
    list_len = len(list_result)
    period_from = int(list_result[0][1])
    period_to = int(list_result[list_len-1][1])
    
    #print(period_from," =>> ",period_to,"\t","total ",list_len,"periods\n")
    return (period_from,period_to,list_len)

    
    
    


def search(n=None):
    if(n == None):
        n = -1
    num = (n,)
    
    
    flag = os.path.exists("rb.sqlite3")
    if(flag == False):
        print("sqlite3 database doesn't exist")
        os.sys.exit()
        
    conn = sqlite3.connect("rb.sqlite3")
    cur = conn.cursor()
    
    
    # select 

    buf_select = cur.execute(
                '''select distinct * from rb order by qishu desc limit ?''',num  ### limit -1 means no limit
                )

 
    tmp = []
    for i in buf_select:
        tmp.append(i)
        
    conn.close()
    
#    for i in tmp:
#        print(i)
    
    return tmp

#===============================================================================
#a = search(-1)
#for i in a:
#    print(i)
#===============================================================================
def search_2(n=None,periods_from=None,periods_to=None):
    '''
     this function implements get the top n from periods_from to periods_to.
     in this function from is greater than to !!!!
     periods_form or to format: 20130** 
    
     if we don't know how to init periods_form and periods_to,
     we may call function from_and_to first...    
    period_from,period_to,list_len = from_and_to()
    print(period_from," =>> ",period_to,"\t","in table total ",list_len,"periods\n")
    '''
    
    if(n == None):
        n = -1

    flag = os.path.exists("rb.sqlite3")
    if(flag == False):
        print("sqlite3 database doesn't exist")
        os.sys.exit()
        
    conn = sqlite3.connect("rb.sqlite3")
    cur = conn.cursor()
    
    
    # select 
#    if(n == -1):
#        num = (n,)
#        buf_select = cur.execute(
#                    '''select  * from rb order by qishu desc limit ?''',num  ### limit -1 means no limit
#                    )


    if(periods_from != None and periods_to != None):
        num = (periods_from,periods_to,n,)
        buf_select = cur.execute(
                    '''select  distinct * from rb 
                     where qishu <= ? 
                    and qishu >= ?
                    order by qishu 
                    desc limit ? ''',num  ### limit -1 means no limit
                    )
    if(periods_from == None and periods_to != None):
        num = (periods_to,n,)
        buf_select = cur.execute(
                    '''select  distinct * from rb 
                    where  qishu >= ?
                    order by qishu 
                    desc limit ? ''',num  ### limit -1 means no limit
                    )
    if(periods_from != None and periods_to == None):
        num = (periods_from,n,)
        buf_select = cur.execute(
                    '''select  distinct * from rb  
                    where qishu <= ? 
                    order by qishu
                    desc limit ? ''',num  ### limit -1 means no limit
                    )
    if(periods_from == None and periods_to == None):
        num = (n,)
        buf_select = cur.execute(
                    '''select  distinct * from rb order by qishu desc limit ?''',num  ### limit -1 means no limit
                    )
    tmp = []
    
    
    for i in buf_select:
        tmp.append(i)
        
    conn.close()


#### write results to file
    #with open('data.txt','w') as f:
        #for i in tmp:
            #f.write(str(i))
            #f.write("\n")
        
    
#    for i in tmp:
#        print(i)
    
    return tmp


def search_3(n=None,periods_from=None,periods_to=None,table_name = "rb"):
    '''
     this function implements get the top n from periods_from to periods_to.
     in this function from is greater than to !!!!
     periods_form or to format: 20130** 
    
     if we don't know how to init periods_form and periods_to,
     we may call function from_and_to first...    
    period_from,period_to,list_len = from_and_to()
    print(period_from," =>> ",period_to,"\t","in table total ",list_len,"periods\n")
    '''
    
    if(n == None):
        n = -1

    flag = os.path.exists("rb.sqlite3")
    if(flag == False):
        print("sqlite3 database doesn't exist")
        os.sys.exit()
        
    conn = sqlite3.connect("rb.sqlite3")
    cur = conn.cursor()
    
    
    # select 
#    if(n == -1):
#        num = (n,)
#        buf_select = cur.execute(
#                    '''select  * from rb order by qishu desc limit ?''',num  ### limit -1 means no limit
#                    )


    if(periods_from != None and periods_to != None):
        num = (periods_from,periods_to,n,)
        buf_select = cur.execute(
                    '''select  distinct * from %s 
                     where qishu <= ? 
                    and qishu >= ?
                    order by qishu 
                    desc limit ? ''' %table_name,num  ### limit -1 means no limit
                    )
    if(periods_from == None and periods_to != None):
        num = (periods_to,n,)
        buf_select = cur.execute(
                    '''select  distinct * from %s 
                    where  qishu >= ?
                    order by qishu 
                    desc limit ? '''  %table_name,num  ### limit -1 means no limit
                    )
    if(periods_from != None and periods_to == None):
        num = (periods_from,n,)
        buf_select = cur.execute(
                    '''select  distinct * from %s 
                    where qishu <= ? 
                    order by qishu
                    desc limit ? '''  %table_name,num  ### limit -1 means no limit
                    )
    if(periods_from == None and periods_to == None):
        num = (n,)
        buf_select = cur.execute(
                    '''select  distinct * from %s order by qishu desc limit ?'''  %table_name,num  ### limit -1 means no limit
                    )
    tmp = []
    
    
    for i in buf_select:
        tmp.append(i)
        
    conn.close()


#### write results to file
    #with open('data.txt','w') as f:
        #for i in tmp:
            #f.write(str(i))
            #f.write("\n")
        
    
#    for i in tmp:
#        print(i)
    
    return tmp
def get_red(n=None,start=None,end=None):
    '''
    return [[1,2,3,4,5.6],...] 
    '''
    t = search_2(n,start,end)
    for i in range(len(t)):
        t[i] = list(t[i])
        t[i].pop(0)
        t[i].pop(0)
        t[i].pop()
    return t
def get_red_2(n=None,start=None,end=None,buf=None):
    '''
    buf should be 9-tuple array
    return [[1,2,3,4,5,6],...] 
    start and end is a must arg
    '''
    if(buf == None):
        print("buf is empty")
        exit(1)
    r = []
    for item in buf:
        item = list(item)
        item.pop(0)
        item.pop(0)
        item.pop()
        r.append(item)
        
    return r
    #if(buf == None):
    #    print("buf is empty")
    #    exit(1)
    #buf = tools.values_copy(buf)
    #t = buf
    #r = []
    #for i in range(len(t)):
    #    t[i] = list(t[i])
    #    t[i].pop(0)
    #    t[i].pop()
    #d = {}
    #for i in range(len(t)):
    #    k = t[i].pop(0)
    #    v = t[i]
    #    d[k] = v 
    #for key in  d.keys():
    #    r.append(d[key])
    #for i in d:
    #    print(i,d[i])
    #    
    ##if(start >= end):
    ##    for i in range(start,end-1,-1):
    ##        #print(i)
    ##        r.append(d[i])
     #
    #return r
def get_blue(n=None,start=None,end=None): 
    '''
    return [] 
    '''
    t = search_2(n,start,end)
    blue = []
    for i in range(len(t)):
        t[i] = list(t[i])
        blue.append(t[i].pop())
    return blue
def get_blue_2(buf=None,n=None,start=None,end=None): 
    '''
    return blue list
    '''
    if(buf == None):
        print("buf empty")
        exit(1)
    r = []
    for item in buf:
        item = list(item)
        r.append(item.pop())
    return r
    
        
    
#===============================================================================
#a = search_2(n=-1)
#for i in a:
#    print(i)
#===============================================================================


#===============================================================================
#a,b = from_and_to()
#print(a,b)
#===============================================================================
if(__name__ == '__main__'):
    a = search_2()
    print(a)