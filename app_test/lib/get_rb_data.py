import re
import sys
import datetime
import logging

MIN_YEAR_RB=2003
DEBUG=False
LOG = logging.getLogger(__file__)
if(sys.version[0] == '2'):
    import urllib
elif(sys.version[0] == '3'):
    from urllib import request as urllib

def search_rb_items(year):
    '''
    return items of one year, range from 2003 to 2014
    '''
    if(year<2003 and year>datetime.date.today.year):
        print("not implemented")
        exit(1)
    source_url = "http://baidu.lecai.com/lottery/draw/list/50?type=range_date&start=%s-01-01&end=%s-12-31" %(year,year)
    try:
        f = urllib.urlopen(source_url)
    except Exception as e:
        print(e)
        LOG.error("access internet web error\t",e)
        return []
    LOG.info("getting data from web...")
    content = f.read()

    if(sys.version[0] == '3'):
        if(isinstance(content,bytes) == True):
            content = content.decode("utf-8")
    souce_format = "<a href=\"/lottery/draw/view/50?phase=2014025\">2014025</a>"
    reg_format1 = re.compile(r"(\s<a\shref=\"/lottery/draw/view/50\?phase=.*>.*</a>\s)")
    reg_format2 = re.compile(r"(\s<tr\sclass.*?</tr>)",flags=re.S)
    reg_format3 = re.compile(r"(\s<tr>\s*?<td>.*?</tr>)",flags=re.S)
    rb_items  = reg_format3.findall(content)
    LOG.info("getting data done from web")
    return rb_items
def get_rb_tuple(rb_item):
    '''
    return ['2003001','2003-02-23','10', '11', '12', '13', '26', '28', '11']
    or []
    :param rb_item:
    :return:
    '''
    r = []
    format_qishu = re.compile(r"\d{7}")
    format_date = re.compile(r"\d{4}-\d{2}-\d{2}")
    format_reds_blues = re.compile(r"(?<=em>)\d{2}")
    res = format_qishu.search(rb_item)
    if(res):
        if DEBUG: print(res.group(0))
        r.append(res.group(0))
    res = format_date.search(rb_item)
    if(res):
        if DEBUG: print(res.group(0))
        r.append(res.group(0))
    res = format_reds_blues.findall(rb_item)
    if(res):
        if DEBUG: print(res)
        r=r+res
        while(len(r)>9):
            r.pop()
    return r
def get_rb_tuples(year):
    '''

    :param year:
    :return [] or :[[],[],[]] inc order
    '''
    rb_items = search_rb_items(year)
    rb_tuple = []
    if(rb_items==None):
        LOG.error("get no data from year %d" %year)
    for rb_item in rb_items:
        item = get_rb_tuple(rb_item)
        if(len(item)):
            rb_tuple.append(item)
    return sorted(rb_tuple)
def search_rb_item(rb_items):
    if(rb_items == None):
        return None
    trs = []
    dict = {}
    ret_items = []
    
    format_date = re.compile(r"(>\d+-\d+-\d+<)")
    format_phase = re.compile(r"(>\d+<)")
    format_numbers = re.compile(r"(>\d{2}<)")
    format_td = re.compile(r"(\s<td.*?</td>)",flags=re.S)
    #import pdb;pdb.set_trace()
    for rb_item in rb_items:
        tds = []
        for  col in format_td.findall(rb_item):
            tds.append(col)
        trs.append(tds) 
    for tds in trs:
        issue_date = format_date.search(tds[0]).group(0).replace(">","").replace("<","")
        issue_phase = format_phase.search(tds[1]).group(0).replace(">","").replace("<","")
        issue_numbers = format_numbers.findall(tds[2])
        for i in range(len(issue_numbers)):
            issue_numbers[i] = issue_numbers[i].replace(">","").replace("<","")
        ret_item = []    
        if(issue_date != None):
            #print(issue_date)
            ret_item.append(issue_date)
        else:
            print("issue_date parse error")
        if(issue_phase != None):
            #print(issue_phase)
            ret_item.append(issue_phase)
        else:
            print("issue_phase parse error")  
        if(issue_numbers != None and len(issue_numbers) == 7):
            for i in issue_numbers:
                ret_item.append(i)
        else:
            print("issue number parse error")
        ret_items.append(ret_item)
    return ret_items
if __name__== '__main__':
    import datetime
    max_year = datetime.date.today().year
    for year in range(MIN_YEAR_RB,max_year+1):
        t = get_rb_tuples(year)
        for i in t:
            with open("rb.txt","a") as f:
                for j in i:
                    f.write(j+"\t")
                f.write("\n")
            print(i)


