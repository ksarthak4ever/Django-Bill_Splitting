from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.salary_month, name='month'),
	path('<slug:salary_slug>/', views.expense_detail, name='detail')
]