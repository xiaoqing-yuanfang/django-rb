# -*- coding:utf-8 -*-
# Create your views here.
#from reportlab.pdfgen import canvas

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response

from models import students
from models import RbData
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
    #return HttpResponse("update OK,Using %d seconds" %(time.time()-now))
    return render_to_response("app_test/app_test.html",{'status':status})
def view_predict_way1(request):
    items = WayOne.getdata()
    return render_to_response("app_test/app_test.html",{'items':items})