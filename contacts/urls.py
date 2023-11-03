from django.urls import path

from contacts.views import list, create, resync


urlpatterns = [

    path('create/', create, name='create'),
    path('resync/', resync, name='resync'),
    path('', list, name='list'),
]
