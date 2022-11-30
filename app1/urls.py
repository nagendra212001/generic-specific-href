from django.urls import path
from app1.views import *
app_name='nagendra'
urlpatterns=[
    path('dj/',dj,name='dj')
]