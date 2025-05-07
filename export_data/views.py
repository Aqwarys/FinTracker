from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
from tracker.models import Transaction
from .forms import ExportDataForm


def export_data(request):
    if request.method == 'POST':
        form = ExportDataForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            transactions = Transaction.objects.filter(date__range=[start_date, end_date])
            df = pd.DataFrame(list(transactions.values()))
            response = HttpResponse(df.to_csv(index=False), content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="transactions.csv"'
            return response
    else:
        form = ExportDataForm()
    return render(request, 'export_data/export_data.html', {'form': form})