"""
URL configuration for html_to_pdf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
   # 1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import GeneratePdf
#from .views import WebpageToPdfView

urlpatterns = [
    path('',views.index,name='index'),
    path('pisa',views.pdf_report,name='pisa_pdf'),
    path('pdf/', GeneratePdf.as_view(), name='generate_pdf'),

    # path('spdf/', save_pdf, name='save_pdf'),
   #path('convert-webpage-to-pdf/', WebpageToPdfView.as_view(), name='convert-webpage-to-pdf'),
]
