from django.shortcuts import render, get_object_or_404
from . models import Salary,Category,Expense


def salary_month(request): # view to select which month's expenses you wanna see
	salary_list = Salary.objects.all()
	return render(request, 'salary-list.html', {'salary_list': salary_list})


def expense_detail(request,salary_slug): # view to see details of expenses done on that month and the remaining salary of the user
	month = get_object_or_404(Salary, slug=salary_slug)
	category_list = Category.objects.filter(month=month)
	return render(request, 'expense-detail.html', {'expense':month, 'expense_list':month.expenses.all(), 'category_list':category_list})