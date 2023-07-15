import os
from datetime import datetime
from django.http import HttpResponse
from django.views.generic import View

from html_to_pdf.utils import render_to_pdf
from django.template.loader import get_template
from django.shortcuts import render
from xhtml2pdf import pisa
from django.conf import settings
from pdfkit import pdfkit, from_url
import asyncio
from pyppeteer import launch

import datetime
from .models import products

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        all_products = products.objects.all()
        image_folder = os.path.join(settings.STATIC_ROOT, 'donor_images')
        image_files = os.listdir(image_folder)
        images = [request.build_absolute_uri(settings.STATIC_URL + 'donor_images/' + file) for file in image_files if file.endswith(('.jpg', '.png', '.jpeg'))]
        data = {
            'date_of_donation': datetime.date.today(),
            'amount': 25,
            'donor_name': 'Cooper Mann',
            'id': 1233434,
            'images': images,
        }
        pdf = render_to_pdf('invoice.html', data,  {'products':all_products})
        return HttpResponse(pdf, content_type='application/pdf')




def index(request):
    image_folder = os.path.join(settings.STATIC_ROOT, 'donor_images')  # Absolute path to the images folder within static files
    image_files = os.listdir(image_folder)
    images = [f'{settings.STATIC_URL}donor_images/{file}' for file in image_files if file.endswith(('.jpg', '.png', '.jpeg'))]



    # pdfkit.from_url('http://127.0.0.1:8000/', 'out.pdf')
    # return HttpResponse('PDF created successfully!')
    return render(request, 'report.html',{'images': images} )




def pdf_report(request):
    all_products = products.objects.all()
    image_folder = os.path.join(settings.STATIC_ROOT, 'donor_images')
    image_files = os.listdir(image_folder)
    images = [request.build_absolute_uri(settings.STATIC_URL + 'donor_images/' + file) for file in image_files if file.endswith(('.jpg', '.png', '.jpeg'))]
    data = {
            'date': datetime.date.today(),
            'meals': 25,
            'name': 'Cooper Mann',
            'id': 1233434,
            'images': images,
        }


    template_path = 'invoice.html'
    context = {
    'products': all_products,
        'data':data,
        'images':images,
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="donar_report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# import os
# from django.http import HttpResponse
# from django.conf import settings
# from reportlab.pdfgen import canvas
#
# def save_pdf(request):
#     # Set the desired path to save the PDF file
#     pdf_path = os.path.join(settings.BASE_DIR, 'media', 'pdf', 'file.pdf')
#
#     # Generate the PDF file using ReportLab or other libraries
#     c = canvas.Canvas(pdf_path)
#     # Add content to the PDF canvas
#
#     # Save and close the PDF canvas
#     c.showPage()
#     c.save()
#
#     # Return the path to the saved PDF file
#     return HttpResponse(pdf_path)
#


import pdfkit

# class WebpageToPdfView(View):
#     def get(self, request, *args, **kwargs):
#         # Get the URL of the webpage to convert
#         webpage_url = 'http://127.0.0.1:8000/'  # Replace with your webpage URL
#
#         # Configure options for PDF generation
#         options = {
#             'quiet': '',
#             'page-size': 'Letter',
#             'margin-top': '0mm',
#             'margin-right': '0mm',
#             'margin-bottom': '0mm',
#             'margin-left': '0mm',
#         }
#
#         # Generate the PDF from the webpage
#         pdf_file = pdfkit.from_url(webpage_url, False, options=options)
#
#         # Return the PDF as a response
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="webpage.pdf"'
#         response.write(pdf_file)
#
#         return response
