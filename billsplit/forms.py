from django import forms

class bill_splitter_form(forms.Form):
	amount = forms.CharField(label='amount', max_length=100)
	number_of_friends=forms.CharField(label='number_of_friends', max_length=100)