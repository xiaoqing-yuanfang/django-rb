import re
import sys
if(sys.version[0] == '2'):
    import urllib
elif(sys.version[0] == '3'):
    from urllib import request as urllib

def search_rb_items(year):
    '''
    return items of one year, range from 2003 to 2014
    '''
    if(year == 2014):
        source_url = "http://baidu.lecai.com/lottery/draw/list/50?agentId=5555"
    elif(year == 2013):
        source_url = "http://baidu.lecai.com/lottery/draw/list/50?d=2013-01-01"
    elif(year == 2012):
        source_url = "http://baidu.lecai.com/lottery/draw/list/50?d=2012-01-01"
    elif(year == 2011):
        source_url = "http://baidu.lecai.com/lottery/draw/list/50?d=2011-01-01"
    elif(year == 2010):
        source_url = "http://baidu.lecai.com/lottery/draw/list/50?d=2010-01-01"
    elif(year == 2009):
        source_url = "http://baidu.lecai.com/lottery/draw/list/50?d=2009-01-01"
    elif(year == 2008):
        source_url = "http://baidu.lecai.com/lottery/draw/list/50?d=2008-01-01"
    elif(year == 2007):
        source_url = "http://baidu.lecai.com/lottery/draw/list/50?d=2007-01-01"
    elif(year == 2006):
        source_url = "http://baidu.lecai.com/lottery/draw/list/50?d=2006-01-01"
    elif(year == 2005):
        source_url = "http://baidu.lecai.com/lottery/draw/list/50?d=2005-01-01"
    elif(year == 2004):
        source_url = "http://baidu.lecai.com/lottery/draw/list/50?d=2004-01-01"
    elif(year == 2003):
        source_url = "http://baidu.lecai.com/lottery/draw/list/50?d=2003-01-01"
    else:
        print("not implemented")
        exit(1)
    f = urllib.urlopen(source_url)
    content = f.read()
    if(sys.version[0] == '3'):
        if(isinstance(content,bytes) == True):
            content = content.decode("utf-8")
    souce_format = "<a href=\"/lottery/draw/view/50?phase=2014025\">2014025</a>"
    reg_format1 = re.compile(r"(\s<a\shref=\"/lottery/draw/view/50\?phase=.*>.*</a>\s)")
    reg_format2 = re.compile(r"(\s<tr\sclass.*?</tr>)",flags=re.S)
    
    rb_items  = reg_format2.findall(content)
    return rb_items
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
if(__name__=="__main__"):
    items = search_rb_items(2004)
    items = search_rb_item(items)
    for i in items:
        print(i)