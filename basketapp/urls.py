from django.urls import re_path, path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    re_path(r'^$', basketapp.basket, name='view'),
    re_path(r'^add/(?P<pk>\d+)/$', basketapp.basket_add, name='add'),
    re_path(r'^remove/(?P<pk>\d+)/$', basketapp.basket_remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basketapp.basket_edit, name='edit')

]
