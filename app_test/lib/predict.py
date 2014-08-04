from app_test.lib import fenxi
#from app_test.lib import sqlite3_op
from app_test.lib import search

def single_minus(six_list,ith):
    '''
    start from 0
    '''
    return six_list[ith+1] - six_list[ith]
def single_sum(six_list,ith):
    '''
    start from 0
    '''
    return six_list[ith+1] + six_list[ith]
def minus_two_two_stat(reds):
    '''
    1    2    3    4    5    6
      m1    m2   m3   m4  m5
    '''
    arr2 = []
    arr3 = []
    for i in range(5):
        arr1 = []
        for j in reds:
            arr1.append(j[i+1] - j[i])
        arr2.append(max(arr1))
        arr2.append(min(arr1))
        arr2.append(sum(arr1)/len(arr1))
        arr3.append(arr2)
    return arr3
def sum_two_two_stat(reds):
    '''
    1    2    3    4    5    6
      m1    m2   m3   m4  m5
    '''
    arr2 = []
    arr3 = []
    for i in range(5):
        arr1 = []
        for j in reds:
            arr1.append(j[i+1] + j[i])
        arr2.append(max(arr1))
        arr2.append(min(arr1))
        arr2.append(sum(arr1)/len(arr1))
        arr3.append(arr2)
    return arr3

def chongfu_stat_all(reds):
    ''' the next period's data can't be 50% the same as its previous nth data '''
    l = len(reds)

    s2 = set()
    
    for i in range(l):
        s1 = set()
        for j in range(i+1,l):
            s1 = set(reds[i]).union(reds[j])
            s2.add(12-len(s1))
    return max(s2),min(s2),sum(s2)/len(s2)

def chongfu_stat_single(red,reds):
    ''' the next period's data can't be 50% the same as its previous nth data '''
    l = len(reds)
    
    s2 = set()
    
    for i in range(l):
        s1 = set()
        s1 = set(reds[i]).union(red)
        s2.add(12-len(s1))
    return max(s2),min(s2),sum(s2)/len(s2)
def minus_sum(reds):
    arr = []
    for i in reds:
        arr.append(i[5]-i[0])
    return (max(arr),min(arr),sum(arr)/len(arr))
def rows_sum(reds):
    arr = []
    for i in reds:
        sum_row = 0
        for j in range(0,6):
            sum_row = sum_row + i[j]
        arr.append(sum_row)
    return (max(arr),min(arr),sum(arr)/len(arr))

def single_minus_sum(red):
    return red[5] - red[0]
def single_row_sum(red):
    sum = 0
    for i in range(6):
        sum = sum + red[i]
    return sum
def stat_every_item(all_reds):
    ''''
    return [(max,min),(max,min),...]
    '''

    arr2 = []

    for i in range(0,6):
        arr1 = []
        arr3 = []
        for j in range(len(all_reds)):
            arr1.append(all_reds[j][i])
        arr3.append(min(arr1))
        arr3.append(max(arr1))
        arr2.append(arr3)
    return arr2   
            
    
    

    
    
    
def all_items_generator():
    ############################
    #### 1th     2th    3th    4th    5th    6th
    #### 1-28   2-29   3-30    4-31   5-32   6-33
    ####  a       b      c       d     e       f
    ############################

    for a in range(1,29):
        for b in range(2,30):
            for c in range(3,31):
                for d in range(4,32):
                    for e in range(5,33):
                        for f in range(6,34):
                            red = [] 
                            red.append(a)
                            red.append(b)
                            red.append(c)
                            red.append(d)
                            red.append(e)
                            red.append(f)
                            if(a < b and b < c and c < d and d < e and e < f):
                                yield red                      
def all_items_generator_opt(arr_scope):
    ###########################
    #### all_scope from function stat_every_item
    ####
    ############################
    #### 1th     2th    3th    4th    5th    6th
    #### 1-28   2-29   3-30    4-31   5-32   6-33
    ####  a       b      c       d     e       f
    ############################

    for a in range(arr_scope[0][0],arr_scope[0][1]):
        for b in range(arr_scope[1][0],arr_scope[1][1]):
            for c in range(arr_scope[2][0],arr_scope[2][1]):
                for d in range(arr_scope[3][0],arr_scope[3][1]):
                    for e in range(arr_scope[4][0],arr_scope[4][1]):
                        for f in range(arr_scope[5][0],arr_scope[5][1]):
                            red = [] 
                            red.append(a)
                            red.append(b)
                            red.append(c)
                            red.append(d)
                            red.append(e)
                            red.append(f)
                            if(a < b and b < c and c < d and d < e and e < f):
                                yield red         
def predict_red_guilv_1(file_name="result.txt",strict_level=30):
    '''
    shuzu must only have 6 unsigned elements
    assumes the next period is x x x x x x.
    and then judge if it acomplishes the guilv before itself.
    strict_level means the return data comply number of strict_level principals from 1 to strict_level
    it is a generator
    '''
    
    ## for validing the next period,we should insert it into sqlite first
    ## and delete it when predict over
    #sqlite3_op.copy_table_items("rb","rb_temp")
    start,end,length = search.from_and_to()
    gen = all_items_generator()
    
    while(True):
        try:
            six_list = gen.next()
        except StopIteration as e:
            break
        if(len(six_list) == 6):
            sqlite3_op.insert_next_period_item_rb_red_predict_version(six_list=six_list)
            
        i = 1
        flag = 1
        while(True):
            cur_max,cur_min,cur_avg = fenxi.guilv_1(full_periods=i,start=start,end=end)
            predict_num = fenxi.num_of_red(n=i,start=start+1,end=start+2-i)
            if(predict_num <= cur_max and predict_num >= cur_min):
                flag += 1
                
            i += 1
            if(cur_avg >= 33):
                break            
        ### 30 means the data comply with at  least 30 kinds of principle from 1 to 30+
        if(flag >= strict_level):
            
            six_list.pop()
            six_list.pop(0)
            six_list.pop(0)
            
            fenxi.save_to_file(file_name,str(six_list))
            yield six_list

    sqlite3_op.copy_table_items("rb_temp","rb")
    
def cur_guilv_1_stat():
    start,end,length = search.from_and_to()
    all_items  = search.search_3()
    
    r =[]
    for i in range(1,34):
        stat = fenxi.guilv_1_optmize(full_periods=i,buf=all_items,start=start,end=end)
        r.append(stat)
    return r

    
def predict_red_guilv_1_optimize_hard(file_name="result.txt",strict_level=30):
    '''
    shuzu must only have 6 unsigned elements
    assumes the next period is x x x x x x.
    and then judge if it acomplishes the guilv before itself.
    strict_level means the return data comply number of strict_level principals from 1 to strict_level
    it is a generator
    strictly comply with the avg value of cur stat
    '''
    
    ## for validing the next period,we should insert it into sqlite first
    ## and delete it when predict over
    #sqlite3_op.copy_table_items("rb","rb_temp")
    start,end,length = search.from_and_to()
    gen = all_items_generator()
    all_items = []
    predict_all_items=[]
    all_items = search.search_3()
    cur_stat = cur_guilv_1_stat()
    
    #for i in cur_stat:
        #fenxi.save_to_file("stat.txt",str(i))

    
    while(True):
        try:
            six_list = gen.next()
            #print("test ",six_list)
        except StopIteration as e:
            break
        if(len(six_list) == 6):
            import copy
            predict_all_items = copy.deepcopy(all_items)  ## important,don't use predict_all_items=all_items
            six_list.append(0)
            six_list.insert(0,start+1)
            six_list.insert(0,0)
            predict_all_items.append(six_list)
            

        

        flag = 0        
        for i in range(1,34):
                      
            predict_num = fenxi.num_of_red_3(buf=predict_all_items,start=start+1,end=start+2-i)
            #fenxi.save_to_file("log.txt",str(predict_num))

            #if(predict_num <= cur_stat[i-1][0] and predict_num >= cur_stat[i-1][1]):
            if(predict_num == cur_stat[i-1][2]):
                flag += 1
        
        fenxi.save_to_file("log.txt",str(six_list)+" "+str(flag))
        ### 30 means the data comply with at  least 30 kinds of principle from 1 to 30+
        if(flag >= strict_level):
            
            six_list.pop()
            six_list.pop(0)
            six_list.pop(0)
            
            fenxi.save_to_file(file_name,str(six_list))
            yield six_list
def predict_red_guilv_1_optimize_easy(file_name="result.txt",strict_level=16):
    '''
    recommended strict_level < 13 and >= 12
    shuzu must only have 6 unsigned elements
    assumes the next period is x x x x x x.
    and then judge if it acomplishes the guilv before itself.
    strict_level means the return data comply number of strict_level principals from 1 to strict_level
    it is a generator
    strictly comply with the avg value of cur stat +- 1
    '''
    
    ## for validing the next period,we should insert it into sqlite first
    ## and delete it when predict over
    ## import pdb;pdb.set_trace()
    start,end,length = search.from_and_to()
    all_items = []
    predict_all_items=[]
    all_items = search.search_3()
    cur_stat = cur_guilv_1_stat()
    #for i in cur_stat:
        #fenxi.save_to_file("stat.txt",str(i))
    arr_set = []
    
    all_reds = search.get_red_2(n=start-end+1,start=start,end=end,buf=all_items)
    items_stat = stat_every_item(all_reds)
    minus_sum_stat = minus_sum(all_reds)
    rows_sum_stat = rows_sum(all_reds)
    all_chongfu_stat = chongfu_stat_all(all_reds)
    stat_minus_two_two = minus_two_two_stat(all_reds)
    stat_sum_two_two = sum_two_two_stat(all_reds)
    gen = all_items_generator_opt(items_stat)
    
    s = set()
    for i in range(1,33):
        s = s.union(set(all_reds[i-1]))
        import copy; s1 = copy.deepcopy(s)
        arr_set.append(s1)
    #for i in arr_set:
        #fenxi.save_to_file("stat.txt",str(i))
    
    
    #for i in cur_stat:
        #fenxi.save_to_file("stat.txt",str(i))

    
    while(True):
        try:
            six_list = gen.next()
        except StopIteration as e:
            break

        flag = 0        
        for i in range(1,33):
            predict_num = len(arr_set[i-1].union(six_list))
            if(predict_num <= cur_stat[i][2] +1 and predict_num >= cur_stat[i][2] -1 ):
                flag += 1
                #fenxi.save_to_file("detail.txt",str(six_list)+" "+str(flag)+" "+  str(predict_num)+ " "+str(cur_stat[i][2]))
        #fenxi.save_to_file("log.txt",str(six_list)+" "+str(flag))
        ### 30 means the data comply with at  least 30 kinds of principle from 1 to 30+
        if(flag >= strict_level \
           and single_minus_sum(six_list)<= minus_sum_stat[0] \
           and single_minus_sum(six_list)>= minus_sum_stat[1] \
           and single_row_sum(six_list) <= rows_sum_stat[0] \
           and single_row_sum(six_list) >= rows_sum_stat[1] \
           and chongfu_stat_single(six_list,all_reds)[0] <= all_chongfu_stat[0] \
           and chongfu_stat_single(six_list,all_reds)[1] >= all_chongfu_stat[1] \
           ):
            for i in range(5):
                if(single_minus(six_list,i) <= stat_minus_two_two[i][0] \
                   and single_minus(six_list,i) >=stat_minus_two_two[i][1] \
                   and single_sum(six_list,i) <= stat_sum_two_two[i][0] \
                   and single_sum(six_list,i) <= stat_sum_two_two[i][0] ):
                    pass
                else:
                    break
            if(i == 4):        
                fenxi.save_to_file(file_name,str(six_list))
                yield six_list
def predict_red_guilv_1_optimize_con(file_name="result.txt",strict_level=30,start=None,end=None,buf=None):
    '''
    cocurrentcy version
    shuzu must only have 6 unsigned elements
    assumes the next period is x x x x x x.
    and then judge if it acomplishes the guilv before itself.
    strict_level means the return data comply number of strict_level principals from 1 to strict_level
    it is a generator
    '''
    
    ## for validing the next period,we should insert it into sqlite first
    ## and delete it when predict over
    #sqlite3_op.copy_table_items("rb","rb_temp")
    #start,end,length = search.from_and_to()
    start = start
    end = end
    gen = all_items_generator()
    all_items = []
    predict_all_items=[]
    all_items = buf
    cur_stat = cur_guilv_1_stat()
    
    #for i in cur_stat:
        #fenxi.save_to_file("stat.txt",str(i))

    r =[]
    while(True):
        try:
            six_list = gen.next()
            #import time;print(time.time())
            #print("test ",six_list)
        except StopIteration as e:
            break
        if(len(six_list) == 6):
            import copy
            predict_all_items = copy.deepcopy(all_items)  ## important,don't use predict_all_items=all_items
            six_list.append(0)
            six_list.insert(0,start+1)
            six_list.insert(0,0)
            predict_all_items.append(six_list)
            

        

        flag = 0        
        for i in range(1,34):
                      
            predict_num = fenxi.num_of_red_3(buf=predict_all_items,start=start+1,end=start+2-i)
            #fenxi.save_to_file("log.txt",str(predict_num))

            #if(predict_num <= cur_stat[i-1][0] and predict_num >= cur_stat[i-1][1]):
            if(predict_num == cur_stat[i-1][2]):
                flag += 1
          
        ### 30 means the data comply with at  least 30 kinds of principle from 1 to 30+
        if(flag >= strict_level):
            
            six_list.pop()
            six_list.pop(0)
            six_list.pop(0)
            
            r.append(six_list)
            fenxi.save_to_file(file_name,str(six_list))
    return r

    
if(__name__ == "__main__"):
    #import pdb;pdb.set_trace()
    gen = predict_red_guilv_1_optimize_hard(strict_level=20)  
    #print(len(cur_guilv_1_stat()))
    #g = all_items_generator()
    #while(True):
        #import time
        #time.sleep(3)
        #print(g.next())
    #import pdb;pdb.set_trace()
    #print(rows_sum([[1,2,3,4,5,6]]))
