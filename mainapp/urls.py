from django.contrib import admin
from django.urls import path
from django.urls import re_path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', mainapp.main, name='main'),
    path('apparel/', mainapp.apparel, name='apparel'),
    path('404/', mainapp.page_not_found, name='page_not_found'),
    path('checkout/', mainapp.checkout, name='checkout'),
    path('contact/', mainapp.contact, name='contact'),
    path('register/', mainapp.register, name='register'),
    re_path(r'^product/(?P<pk>\d+)/$', mainapp.product, name='product'),
]
