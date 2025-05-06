from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Transaction, Category
from .forms import TransactionForm, UpdateTransactionForm


from django_filters.views import FilterView
from .filters import TransactionFilter

def index(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            form = TransactionForm()
            return redirect('tracker:index')
    else:
        form = TransactionForm()
    f = TransactionFilter(request.GET, queryset=Transaction.objects.all())
    category = Category.objects.all()

    context = {
        'form': form,
        'transactions': f.qs,
        'category': category,
        'filter': f,
    }
    return render(request, 'tracker/index.html', context)


def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    return redirect('tracker:index')

def update_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)

    if request.method == 'POST':
        form = UpdateTransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('tracker:index')
        else:
            print(form.errors)
    else:
        form = UpdateTransactionForm(instance=transaction)

    context = {
        'form': form,
        'transaction': transaction
    }
    return render(request, 'tracker/update_transaction.html', context=context)
