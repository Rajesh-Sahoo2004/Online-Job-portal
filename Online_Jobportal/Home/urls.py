from django.urls import path,include

from Home import admin
from Home.views import *

urlpatterns = [
    path('',dashboard, name="dashboard"),
    path('about/',about, name="about"),
    path('contact/',contact,name="contact"),
    path('faq/',faq, name="faq"),

]