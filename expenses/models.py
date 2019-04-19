from django.db import models
from django.utils.text import slugify


class Salary(models.Model): #To store monthly salary of the user
	month_name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True, blank=True)
	salary = models.IntegerField()

	def save(self, *args,**kwargs): #overwriting save method to automatically create slug depending on project name
		self.slug = slugify(self.month_name)
		super(Salary, self).save(*args, **kwargs) #calling the actual save method for the class

	def __str__(self):
		return '{}'.format(self.month_name)

	def salary_left(self):
		expense_list = Expense.objects.filter(month=self)
		total_expense_amount = 0
		for expense in expense_list:
			total_expense_amount += expense.amount

		return self.salary - total_expense_amount

	def total_transactions(self):
		expense_list = Expense.objects.filter(project=self)
		return len(expense_list)

class Category(models.Model): #Model for Category of expense
	month = models.ForeignKey(Salary, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.name)

class Expense(models.Model): #Model for Expense details
	month = models.ForeignKey(Salary, on_delete=models.CASCADE, related_name='expenses')
	title = models.CharField(max_length=100)
	amount = models.DecimalField(max_digits=8, decimal_places=0)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	class Meta:
		ordering = ('-amount',)

	def __str__(self):
		return '{}'.format(self.title)