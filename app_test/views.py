# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from models import students
from reportlab.pdfgen import canvas

def just_test(request):
    record = students.objects.get(stu_id=1)
    if(record == None):
        print(" record empty")
    else:
        print(record)
    #import pdb;pdb.set_trace()
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