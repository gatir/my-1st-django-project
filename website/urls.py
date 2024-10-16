
from django.urls import path
from website.views import *

app_name = 'website'
urlpatterns = [

    path('', index_view, name='index'),
    # path('index.html', index_view),
    path('about', about_view, name='about'),
    # path('about.html', about_view),
    path('contact', contact_view, name='contact'),
]
