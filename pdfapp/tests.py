import os
from datetime import datetime
from django.http import HttpResponse
from django.views.generic import View

from html_to_pdf.utils import render_to_pdf #created in step 4

import datetime


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        image_folder = os.path.join(settings.STATIC_ROOT, 'donor_images')  # Absolute path to the images folder within static files
        image_files = os.listdir(image_folder)
        images = [f'{settings.STATIC_URL}donor_images/{file}' for file in image_files if file.endswith(('.jpg', '.png', '.jpeg'))]
        data = {
            'today': datetime.date.today(),  # Use as a property, not a method
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('invoice.html', {'images':images} )
        return HttpResponse(pdf, content_type='application/pdf')


import os
import pdfkit
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
from django.shortcuts import render

from django.conf import settings
from pdfkit import pdfkit, from_url
import asyncio
from pyppeteer import launch



def index(request):
    image_folder = os.path.join(settings.STATIC_ROOT, 'donor_images')  # Absolute path to the images folder within static files
    image_files = os.listdir(image_folder)
    images = [f'{settings.STATIC_URL}donor_images/{file}' for file in image_files if file.endswith(('.jpg', '.png', '.jpeg'))]


    # pdfkit.from_url('http://127.0.0.1:8000/', 'out.pdf')
    # return HttpResponse('PDF created successfully!')
    return render(request, 'report.html', {'image': images})

