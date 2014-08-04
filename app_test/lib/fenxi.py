#### analysise the data from rb.sqlite3####


#### because every 34 period can possiblly cover all red, so blue

#### this programm is based on the theroy that it is random that repetition frequency is so low
#### that we think that the next period will come what the previous N(5-10) period not show.

#### moreover, we should also track the trend of the every data, but it will not implemented 
#### lately



#### we assume that 7 period

#### analyse result of the nearest N periods
#### 1. 1-34 the number

#!/usr/bin/python
# -*- coding: <utf-8> -*-

from app_test.lib import tools
from app_test.lib  import search
### statistics of rates of all data in recent N periods


### make next item the last item of recent

#### this function implements fenxi of period M to period N and save the result to file file_name
#### here we assume 1-11 as stage 1, 12-22 as stage 2, 23-33 as stage 3
def stages_fenxi(n = None,periods_from=None,periods_to=None,file_name="all.txt"): 
    import search
    tmp = search.search_2(n,periods_from,periods_to)

    stage1_sum = 0
    stage2_sum = 0
    stage3_sum = 0

    for i in tmp:
        #### we here only consider the red 
        stage1_i = 0
        stage2_i = 0
        stage3_i = 0
        for j in range(2,8):
            if(i[j] <= 11 and i[j] >= 1):
                stage1_i += 1 
            if(i[j] <= 22 and i[j] >= 12):
                stage2_i += 1 
            if(i[j] <= 33 and i[j] >= 23):
                stage3_i += 1 
        str_to_save = str(i[1])+" "+str(stage1_i)+" "+str(stage2_i)+" "+str(stage3_i)
        save_to_file(file_name,str_to_save)
        stage1_sum += stage1_i
        stage2_sum += stage2_i
        stage3_sum += stage3_i

    str_to_save = "all    "+" "+str(stage1_sum)+" "+str(stage2_sum)+" "+str(stage3_sum)
    save_to_file(file_name,str_to_save)

### this function recv data from sqlite
### and returns chart data

#from pychart import *
#def generate_to_chart(data_from_sqlite,cycle_dir):
##	import pdb;pdb.set_trace()
    #len_of_data = len(data_from_sqlite)
    #tmp = []
    #for i in range(len_of_data):
        #tmp_item = list(data_from_sqlite[i])
        #tmp_item.pop(0)
        #tmp_item[0] = tmp_item[0]-2013000
        #tmp_item = tuple(tmp_item)
        #tmp.append(tmp_item)
    #import pychart_me
    #import os
    #import signal
####### the number of processes forked is more than you want if you do it this way#################
##	for i in range(7):
##		#import pdb;pdb.set_trace()
##		print("waiting for %dth processes to end" %(i+1))
##		pdf_name = str(cycle_dir)+"_"+str(i+1)+".pdf"
##		pid = os.fork()
##		if(pid == 0):
##			#pychart_me.pychart_rb(sorted(tmp),pdf_name,i+1)
##			pass
##		else:
##			os.wait()
######################################################################################################

    ##import pdb;pdb.set_trace()
    #print("waiting for 1th processes to end")
    #pdf_name = str(cycle_dir)+"_"+str(1)+".pdf"
    #pid = os.fork()
    #if(pid == 0):
        #pychart_me.pychart_rb(sorted(tmp),pdf_name,1)
        #os.sys.exit()
        #pass
    #else:
        #os.wait()

        #print("waiting for 2th processes to end")
        #pdf_name = str(cycle_dir)+"_"+str(2)+".pdf"
        #pid = os.fork()
        #if(pid == 0):
            #pychart_me.pychart_rb(sorted(tmp),pdf_name,2)
            #os.sys.exit()
            #pass
        #else:
            #os.wait()

            #print("waiting for 3th processes to end")
            #pdf_name = str(cycle_dir)+"_"+str(3)+".pdf"
            #pid = os.fork()
            #if(pid == 0):
                #pychart_me.pychart_rb(sorted(tmp),pdf_name,3)
                #os.sys.exit()
                #pass
            #else:
                #os.wait()
                #print("waiting for 4th processes to end")
                #pdf_name = str(cycle_dir)+"_"+str(4)+".pdf"
                #pid = os.fork()
                #if(pid == 0):
                    #pychart_me.pychart_rb(sorted(tmp),pdf_name,4)
                    #os.sys.exit() ### maybe this cluase flush child process's stdout 
                    #pass
                #else:
                    #os.wait()

                    #print("waiting for 5th processes to end")
                    #pdf_name = str(cycle_dir)+"_"+str(5)+".pdf"
                    #pid = os.fork()
                    #if(pid == 0):
                        #pychart_me.pychart_rb(sorted(tmp),pdf_name,5)
                        #os.sys.exit() ### maybe this cluase flush child process's stdout 
                        #pass
                    #else:
                        #os.wait()
                        #print("waiting for 6th processes to end")
                        #pdf_name = str(cycle_dir)+"_"+str(6)+".pdf"
                        #pid = os.fork()
                        #if(pid == 0):
                            #pychart_me.pychart_rb(sorted(tmp),pdf_name,6)
                            #os.sys.exit() ### maybe this cluase flush child process's stdout 
                            #pass
                        #else:
                            #os.wait()
                            #print("waiting for 7th processes to end")
                            #pdf_name = str(cycle_dir)+"_"+str(7)+".pdf"
                            #pid = os.fork()
                            #if(pid == 0):
                                #pychart_me.pychart_rb(sorted(tmp),pdf_name,7)
                                #os.sys.exit() ### maybe this cluase flush child process's stdout 
                                #pass
                            #else:
                                #os.wait()


def store_cylce_to_sqlite(data_of_one_cycle):
    # here use the temp table in sqlite3 named "temp" which the author named it
    # and it is created in advance in test.py

    #import pdb;pdb.set_trace() 

    import sqlite3
    import os
    flag = os.path.exists("rb.sqlite3")
    if(flag == False):
        print("sqlite3 database doesn't exist")
        os.sys.exit()

    conn = sqlite3.connect("rb.sqlite3")
    cur = conn.cursor()

    cur.execute(
        '''delete from temp'''
    )
    for i in range(len(data_of_one_cycle)):
        str_to_insert = (data_of_one_cycle[i][0],data_of_one_cycle[i][1],
                         data_of_one_cycle[i][2],data_of_one_cycle[i][3])
        cur.execute(
            '''insert into temp values(?,?,?,?)''',str_to_insert
        )
    conn.commit()
    conn.close()


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


def save_to_file(file_name,s):
    import os
    
    if(file_name == None):
        return False
    import datetime
    t = str(datetime.datetime.now()).ljust(29)
    s = t+ str(s)
    with open(file_name,'a') as f:
        f.write(s)
        f.write('\n')


def rates(n = None,periods_from=None,periods_to=None): ###### default all records 

    flag_no_complete_cycle = False
    if(n == 'un'):
        flag_no_complete_cycle = True
        n = None


    import search
    tmp = search.search_2(n,periods_from,periods_to)
    rows = len(tmp)


    red_all = []
    un_show = []
    for i in range(1,34):
        red_all.append(i)
    hits =[0]*33 #34 number


    for i in tmp:
        for j in range(2,8):
            for k in range(1,34):
                if(i[j] == k):
                    hits[k-1] += 1

    print("rates function\n")
    save_to_file("log.txt","rates function\n")

    if(flag_no_complete_cycle == True):
        print("uncomplet cycle\n")
        save_to_file("log.txt","uncomplet cycle\n")
    else:
        print("complete cycle\n")
        save_to_file("log.txt","complet cycle\n")
    for i in zip(red_all,hits):
        i = list(i)
        #import pdb;pdb.set_trace()
        i.append(rows)
        i.append(str(i[1]/i[2])[0:5])   #### truncate long decimal point
        i[0] = str(i[0]).zfill(2)
        i[1] = str(i[1]).zfill(3)
        i[2] = str(i[2]).zfill(3)
        if(i[3] == '0.0'):
            un_show.append(i[0])
        print(i)
        save_to_file("log.txt",str(i))
    print("\nnumbers that un_show\n",un_show)
    save_to_file("log.txt","\nnumbers that un_show\n:%s\n" %(un_show))
    del tmp
    ###### default all records 
def rates_file(n = None,periods_from=None,periods_to=None,file_name="all.txt",results_of_all_cycles=None,flag_gen_chart=False): 
    '''this function fenxi factors of data from period M to period N and save them to file file_name'''

    #### firstly delete all previous data
    import os
    if(os.path.exists(file_name)):
        os.remove(file_name)

    if(results_of_all_cycles != None):
        save_to_file(file_name,"results  of all cycle\n--------------------------------------")
        for i in results_of_all_cycles:
            save_to_file(file_name,str(i))
        save_to_file(file_name,"--------------------------------------")

    save_to_file(file_name,str("\nthis cycle has"+"------------"+str(n)+"items-----------------\n"))


    flag_no_complete_cycle = False
    if(n == 'un'):
        flag_no_complete_cycle = True
        n = None


    import search
    tmp = search.search_2(n,periods_from,periods_to)
    ####### write contents of tmp to file
    for i in tmp:
        i = str(i)
        save_to_file(file_name,i)
##### here generate the pdf chart file
    #pdf_name = file_name.replace('txt','pdf')
    cycle_dir = file_name.replace('.txt','')
    if(flag_gen_chart == True):
        pass
        generate_to_chart(tmp,cycle_dir)

    #generate_to_chart(tmp,pdf_name)

##### here generate the pdf chart file

    rows = len(tmp)

    data_of_one_cycle = []
    red_all = []
    un_show = []
    for i in range(1,34):
        red_all.append(i)
    hits =[0]*33 #34 number


    for i in tmp:
        for j in range(2,8):
            for k in range(1,34):
                if(i[j] == k):
                    hits[k-1] += 1

    #print("rates function\n")
    save_to_file(file_name,"rates function\n")

    if(flag_no_complete_cycle == True):
        #print("uncomplet cycle\n")
        save_to_file(file_name,"uncomplet cycle\n")
    else:
        #print("complete cycle\n")
        save_to_file(file_name,"complet cycle\n")
    for i in zip(red_all,hits):
        i = list(i)
        #import pdb;pdb.set_trace()
        i.append(rows)
        i.append(str(i[1]/i[2])[0:5])   #### truncate long decimal point
        i[0] = str(i[0]).zfill(2)
        i[1] = str(i[1]).zfill(3)
        i[2] = str(i[2]).zfill(3)
        if(i[3] == '0.0'):
            un_show.append(i[0])
        #print(i)
        data_of_one_cycle.append(i)
        save_to_file(file_name,str(i))

    #print("\nnumbers that un_show\n",un_show)
    save_to_file(file_name,"\nnumbers that un_show\n:%s\n" %(un_show))
    del tmp

    store_cylce_to_sqlite(data_of_one_cycle)
    #import pdb;pdb.set_trace()
    chongfucishufenxi = fenxi_cycle_from_sqlite()
    for i in chongfucishufenxi:
        save_to_file(file_name,str(i))

### here we want to fenxi 1-11,12-22,23-33's rates
    save_to_file(file_name,"stages_fenxi begin")
    stages_fenxi(n,periods_from,periods_to,file_name) 
    save_to_file(file_name,"stages_fenxi end")


    import datetime

    str_time = "\n\n\n"+str(datetime.datetime.now())+"\n"
    save_to_file(file_name,str_time)


#rates()

### statistics of how many periods are a cycle in recent N periods 

### in this cycle, about 90% data from 1 to 33 are shown, and in its
### previous cycle, about 90% data are the same as its next cycle. 
### we assume this as a cycle, not a accurate figure.


#### we should implement the function so that it can
#### search periods from m to n
#### so we should add two Parameter in function
#### this function retuns an triple array [num,period_from,period_to]
def cycle(n = None,periods_from=None,periods_to=None, hits_rate_of_34 = 0.9):
    print("results when hits_rate_of_34 == %.2f" %hits_rate_of_34)
    #save_to_file("log.txt","results when hits_rate_of_34 == %.2f" %(hits_rate_of_34))

    import search

    tmp = search.search_2(n, periods_from, periods_to)

    if(periods_from == None and periods_to == None):
        from_p,to_p,len = search.from_and_to()
    else:
        from_p = periods_from
        to_p = periods_to
        len = n

    red_all = []
    for i in range(1,34):
        red_all.append(i)

    hits =[0]*33 #34 number
    periods_a_cycle = 0
    cycles = 0
    from_per_cycle = ""
    global cycyle_change
    cycle_change = True
    #last_period = 0
    return_results = []

    for i in tmp:
        if(cycle_change == True):
            from_per_cycle = i[1]

        cycle_change = False


        periods_a_cycle += 1
        for j in range(2,8):
            for k in range(1,34):
                if(i[j] == k):
                    hits[k-1] += 1

        num = 0
        for k in range(0,33):
            if(hits[k] != 0):
                num += 1

#        import pdb;pdb.set_trace()  
        if( num/33.0 > hits_rate_of_34 ):
#            import pdb;pdb.set_trace() 
            cycles += 1
#            print("%d. clycle\t %d periods_a_cycle" %(cycles,periods_a_cycle))
#            print(from_per_cycle,"==>>",i[1],"\n")
            return_results.append([periods_a_cycle,from_per_cycle,i[1]])
            print(cycles,": ",from_per_cycle,"==>>",i[1],"  ",periods_a_cycle,"periods_a_cycle")

            last_period = i[1]
            periods_a_cycle = 0


            hits =[0]*33
            cycle_change = True



#            break;
#    import pdb;pdb.set_trace()
    if(cycle_change == True and last_period == to_p):
        print("there is no uncomplete cycle\n")
    elif(cycle_change == False and 'last_period' in dir()):
        print("\nun:  %s ==>> %s    %d periods uncompleted\n"
              %(int(last_period-1),to_p,int(last_period)-int(to_p)))
        return_results.append(['un',last_period-1,to_p])
    else:
        print("\nun:  %s ==>> %s    %d periods uncompleted\n"
              %(int(from_p),to_p,int(from_p)-int(to_p)+1))
        return_results.append(['un',from_p,to_p])     

    return return_results


def fenxi_from_to_cycle_rates(n=None,periods_from=None,periods_to=None,hits_rate_of_34=0.8,flag_gen_chart=False):
#import pdb;pdb.set_trace()
### here attention
### the number n must equal periods_from-periods_to+1
    a = cycle(n,periods_from,periods_to,hits_rate_of_34)
    #import pdb;pdb.set_trace()
    import os
    if(a == []):
        print("no result returned")
    else:
        dir_name = str(a[0][1])+"-"+str(a[len(a)-1][2])

        if(os.path.exists(dir_name)):
            cmd = "rm -rf "+ dir_name
            os.system(cmd)
        if(os.path.exists(dir_name) == False):
            os.mkdir(dir_name)
            for i in range(len(a)):
                print("i %d" %i)
            #    import pdb;pdb.set_trace()
                dir_name_level2= str(a[i][1])+"-"+str(a[i][2])
                dir_name_level2 = os.path.join(dir_name,dir_name_level2)
                if(os.path.exists(dir_name_level2)):
                    #cmd = "rm -rf "+ dir_name_level2
                    #os.system(cmd)
                    pass
                else:

                    os.mkdir(dir_name_level2)
                    print("makeing dir %s" %dir_name_level2)

                    f_name = str(a[i][1])+"-"+str(a[i][2])+".txt"
                    f_name = os.path.join(dir_name_level2,f_name)

                    rates_file(a[i][0],a[i][1],a[i][2],f_name,a,flag_gen_chart)


def stdout_to_null():
    import os
    file_open = open("/dev/null","w")
    os.dup2(file_open.fileno(),os.sys.stdout.fileno())

    #stdout_to_null()

#fenxi_from_to_cycle_rates(n=46,periods_from=2013055,periods_to=2013010,hits_rate_of_34=0.8)
#import chart_pdf_modified
#chart_pdf_modified.modify_pdf()
#import pdb;pdb.set_trace()
#a = cycle(n=10,periods_from=2013052,periods_to=2013043,hits_rate_of_34=0.8)
#print(a)
#
#a = cycle(n=8,periods_from=2013052,periods_to=2013045,hits_rate_of_34=0.8)
#
#import os
#if(a == []):
#        print("no result returned")
#else:
#        dir_name = str(a[0][1])+"-"+str(a[len(a)-1][2])
#   
#        if(os.path.exists(dir_name)):
#            print("------------------------------------------")
#            print("the dir of this cycles have exist")
#            print("------------------------------------------")
#        else:
#            os.mkdir(dir_name)
#            for i in range(len(a)):
#            #    import pdb;pdb.set_trace()
#            
#                f_name = str(a[i][1])+"-"+str(a[i][2])+".txt"
#                f_name = os.path.join(dir_name,f_name)
#            
#                rates_file(a[i][0],a[i][1],a[i][2],f_name,a)

def rate_of_red(n= None,start = None, end = None):
    import search 
    ''' chuxian cishu /34 from start to end'''
    #if(start == None or end == None):
        #return 0
    t = search.get_red(n,start,end)
    nums = []
    for i in range(33):
        nums.append(i+1)

    for i in range(len(t)):
        for j in range(6):
            if(t[i][j] in nums):
                nums[t[i][j]-1] = 0
    return nums.count(0)/(33.0)

def num_of_red(n= None,start = None, end = None):
    import search 
    ''' chuxian cishu /34 from start to end'''
    #if(start == None or end == None):
        #return 0
    t = search.get_red(n,start,end)
    nums = []
    for i in range(33):
        nums.append(i+1)

    for i in range(len(t)):
        for j in range(6):
            if(t[i][j] in nums):
                nums[t[i][j]-1] = 0
    return nums.count(0)
def num_of_red_2(n=None,start = None, end = None,buf=None):
    '''buf should be 9-tuple shuzu'''
    ''' chuxian cishu /34 from start to end'''
    import tools
    buf = tools.values_copy(buf)    
    import search
    #if(start == None or end == None):
        #return 0
        

    t = search.get_red_2(n,start,end,buf)

    nums = []
    for i in range(33):
        nums.append(i+1)

    for i in range(len(t)):
        for j in range(6):
            if(t[i][j] in nums):
                nums[t[i][j]-1] = 0
    return nums.count(0)

def num_of_red_3(n=None,start = None, end = None,buf=None):
    '''buf should be 9-tuple shuzu'''
    ''' chuxian cishu /34 from start to end'''
    buf = tools.values_copy(buf)    
    t = search.get_red_2(n,start,end,buf)
    s = set()
    for i in t:
        s = s.union(set(i))
    return len(s)

def guilv_1(full_periods = 1,start=None,end=None,file_name = None):
    '''
    returns max,min,avg value of one full_periods
    
    results show that in any N periods 
    number rates are closely equal to 1.0
    *********
    we should seek for genernal pricipal,just like this one,etc every n periods,consecutively
    *********
    '''
    import search
    full_periods = full_periods 
    list_temp = []
    if(start == None and end == None):
        start_all,end_all,length_all = search.from_and_to()
    else:
        start_all = start
        end_all = end
        length_all = start-end+1
    start = start_all
    end = start-full_periods + 1
    while(end >= end_all):

        a = num_of_red(full_periods,start,end)
        list_temp.append(a)
        
#        print("%d-->%d:%d" %(start,end,a))
        
        s = "%d-->%d:%d" %(start,end,a)
        save_to_file(file_name,s)
        start = start - 1
        end = start-full_periods + 1	

    max_item = max(list_temp)
    s = "max value " + str(max_item)
    save_to_file(file_name,s)
    
    min_item = min(list_temp)
    s = "min_value " + str(min_item)
    save_to_file(file_name,s)
    
    avg = sum(list_temp)/len(list_temp)
    s = "avg value " + str(avg)
    save_to_file(file_name,s)
    
    return (max_item,min_item,avg)

def guilv_1_optmize(full_periods = 1,buf=None,start=None,end=None,file_name = None):
    '''
    returns max,min,avg value of one full_periods
    buf should be 9-tuple array
    results show that in any N periods 
    number rates are closely equal to 1.0
    *********
    we should seek for genernal pricipal,just like this one,etc every n periods,consecutively
    *********
    '''
    buf = tools.values_copy(buf)
    
    full_periods = full_periods 
    list_temp = []
    if(start == None and end == None):
        start_all,end_all,length_all = search.from_and_to()
    else:
        start_all = start
        end_all = end
        length_all = start-end+1
    start = start_all
    end = start-full_periods + 1
    while(end >= end_all):

        a = num_of_red_3(start=start,end=end,buf=buf)
        list_temp.append(a)
        
#        print("%d-->%d:%d" %(start,end,a))
        
        s = "%d-->%d:%d" %(start,end,a)
        save_to_file(file_name,s)
        start = start - 1
        end = start-full_periods + 1	

    max_item = max(list_temp)
    s = "max value " + str(max_item)
    save_to_file(file_name,s)
    
    min_item = min(list_temp)
    s = "min_value " + str(min_item)
    save_to_file(file_name,s)
    
    avg = sum(list_temp)/len(list_temp)
    s = "avg value " + str(avg)
    save_to_file(file_name,s)
    
    return (max_item,min_item,avg)

def nums_of_reds(buf,start,end):
    '''
    take 9-tuple array as parameter return an dict object like
    {qishu,...}
    '''
    d = {}

    for i in range(start,end-1,-1):
        arr =[]
        for j in range(start,end-1,-1):
            num = num_of_red_2(start=j,end=end,buf=buf,n=start-end+1)
            arr.append(num)
        d[i] = arr
    return d

        
if(__name__ == "__main__"):
    import os
    if(os.path.exists("temp")):
        for i in os.listdir("temp"):
            p = os.path.join("temp",i)
            os.remove(p)

        os.removedirs("temp")
    else:
        os.mkdir("temp")

    for i in range(1,33):
        file_name = os.path.join(os.getcwd(),"temp"+"/"+str(i)+".txt")
        save_to_file(file_name,str(i))
        guilv_1(full_periods=i,file_name = file_name)

