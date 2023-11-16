from srilanka.views import *
from django.urls import path
app_name='anu'
urlpatterns=[
    path('black/',black,name='black'),
]