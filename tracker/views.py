from django.shortcuts import render, redirect
from .models import Transaction, Category
from .forms import TransactionForm


def index(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            form = TransactionForm()
            return redirect('tracker:index')
    else:
        form = TransactionForm()

    transactions = Transaction.objects.all()
    category = Category.objects.all()

    context = {
        'form': form,
        'transactions': transactions,
        'category': category
    }
    return render(request, 'tracker/index.html', context)
