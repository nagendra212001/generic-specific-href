from django.urls import path
from app2.views import *
app_name='babu'
urlpatterns=[
    path('tillu/',tillu,name='tillu')
]