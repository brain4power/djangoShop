from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static


app_name = 'mainapp'

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$', mainapp.main, name='main'),
    url(r'^apparel/$', mainapp.apparel, name='apparel'),
    url(r'^404/$', mainapp.page_not_found, name='page_not_found'),
    url(r'^checkout/$', mainapp.checkout, name='checkout'),
    path('contact/', mainapp.contact, name='contact'),
    # url(r'^login/$', mainapp.login, name='login'),
    url(r'^register/$', mainapp.register, name='register'),
    url(r'^product/(?P<pk>\d+)/$', mainapp.product, name='product'),
    url(r'^auth/', include('authapp.urls', namespace='auth')),
]
