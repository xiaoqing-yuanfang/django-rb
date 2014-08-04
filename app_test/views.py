# -*- coding:utf-8 -*-
# Create your views here.
from reportlab.pdfgen import canvas

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response

from models import students


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


def rb(request):
    items = []
    for i in range(1000):
        items.append(i)
    return render_to_response("app_test/app_test.html", {"items": items, })