from django.shortcuts import render
from . forms import bill_splitter_form


def splitter(request):
    if request.method == 'POST':
        form = bill_splitter_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            amount=form['amount'].value()
            amount=int(amount)
            number_of_friends=form['number_of_friends'].value()
            number_of_friends =int(number_of_friends)
            answer=amount/number_of_friends #dividing bill equally among friends
            return render(request, 'billsplitter.html', {'answer':answer})

    else: #if form is not valid simply returning a blank form
        form=bill_splitter_form()
    return render(request,'billsplitter.html',{'form':form})