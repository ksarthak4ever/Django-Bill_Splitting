from django.urls import path
from . import views


urlpatterns = [
    path('',views.splitter,name='splitter'),
]