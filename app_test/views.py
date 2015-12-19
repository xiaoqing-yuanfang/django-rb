# -*- coding:utf-8 -*-
# Create your views here.
#from reportlab.pdfgen import canvas

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response

from models import students
from models import RbData
from models import RData
from models import BData
from lib.get_rb_data import  get_rb_tuples
from lib.get_rb_data import MIN_YEAR_RB
from lib.lib_wayone import WayOne
import datetime
import time
import threading


flag_thread_upd_database = False
def just_test(request):
    record = students.objects.get(stu_id=1)
    if (record == None):
        print(" record empty")
    else:
        print(record)
    # import pdb;pdb.set_trace()
    from django.core.mail import send_mail

    send_mail("subject", "nihao", "gcy3y@163.com", ["gcy3y@163.com"])
    return redirect(record)


def pdf_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


def helloword(request):
    return render_to_response("app_test/app_test.html")


def update_database():
    now = time.time()
    max_year = datetime.date.today().year
    for year in range(MIN_YEAR_RB,max_year+1):
        items_year = get_rb_tuples(year)
        for item in items_year:
            item_db = RbData(item[0],item[1],item[2],item[3],item[4],
                             item[5],item[6],item[7],item[8])
            item_db.save()
    status = "update OK,Using %f seconds" %(time.time()-now)
    print(status)
    #return HttpResponse("update OK,Using %d seconds" %(time.time()-now))
    #return render_to_response("app_test/app_test.html",{'status':status})
def thr_update_database():
    '''
    update databse every date's 21 oclock
    :return:
    '''
    while(True):
        hour = datetime.datetime.now().hour
        if(hour==9):
            update_database()
        time.sleep(3600)

def rb(request):
    global flag_thread_upd_database
    items = []
    if(flag_thread_upd_database==False):
        thr1 = threading.Thread(target=thr_update_database)
        thr1.start()
        flag_thread_upd_database = True
    return render_to_response("app_test/app_test.html", {"items": items, })

def view_update_database(request):
    now = time.time()
    max_year = datetime.date.today().year
    for year in range(MIN_YEAR_RB,max_year+1):
        items_year = get_rb_tuples(year)
        for item in items_year:
            item_db = RbData(item[0],item[1],item[2],item[3],item[4],
                             item[5],item[6],item[7],item[8])
            item_db.save()
    status = "update OK,Using %f seconds" %(time.time()-now)
    update_r_data()
    update_b_data()
    #return HttpResponse("update OK,Using %d seconds" %(time.time()-now))
    return render_to_response("app_test/app_test.html",{'status':status})
def view_predict_way1(request):
    items = WayOne.get_r_data()
    return render_to_response("app_test/show_result.html",
                              {"predict_way":"way_1",'items':items})

def update_r_data():
    for line in RbData.objects.all():
        d = {}
        for i in range(1,34):
            tmp ={i:0}
            d.update(tmp)

        for i in range(1,34):
            l =[]
            l.append(line.r1)
            l.append(line.r2)
            l.append(line.r3)
            l.append(line.r4)
            l.append(line.r5)
            l.append(line.r6)
            if(i in l):
                d[i]=1
        item_rdata = RData(qishu=line.qishu,riqi=line.riqi,r1=d[1],r2=d[2],
                           r3=d[3],r4=d[4],r5=d[5],r6=d[6],r7=d[7],r8=d[8],
                           r9=d[9],r10=d[10],r11=d[11],r12=d[12],r13=d[13],
                           r14=d[14],r15=d[15],r16=d[16],r17=d[17],r18=d[18],
                           r19=d[19],r20=d[20],r21=d[21],r22=d[22],r23=d[23],
                           r24=d[24],r25=d[25],r26=d[26],r27=d[27],r28=d[28],
                           r29=d[29],r30=d[30],r31=d[31],r32=d[32],r33=d[33])
        item_rdata.save()
    print("table rdata update OK")

def update_b_data():
    for line in RbData.objects.all():
        d = {}
        for i in range(1,17):
            tmp ={i:0}
            d.update(tmp)
        d[line.b1] = 1

        item_bdata = BData(qishu=line.qishu,riqi=line.riqi,b1=d[1],b2=d[2],
                           b3=d[3],b4=d[4],b5=d[5],b6=d[6],b7=d[7],b8=d[8],
                           b9=d[9],b10=d[10],b11=d[11],b12=d[12],b13=d[13],
                           b14=d[14],b15=d[15],b16=d[16])
        item_bdata.save()
    print("table bdata update OK")