from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^categories/(?P<category_slug>[-\w]+)/$',
        product_list,name='product_list_by_category'),
    url('register', register),
    url('login', login),
    url('logout', user_logout),
    url(r'^$', product_list, name='product_list'),
    url(r'^basket_adding$', basket_adding, name='basket_adding'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        product_detail,name='product_detail'),
    url('about', about),
    url(r'^checkout$', checkout, name='checkout'),
    url('profile_edit', profile_edit, name='profile_edit'),
]