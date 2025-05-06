import django_filters
from .models import Transaction
from django_filters.widgets import RangeWidget

class TransactionFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter(
        widget=RangeWidget(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Transaction
        fields = {
            'operation_type': ['exact'],
            'category': ['exact'],
            'date': ['exact'],
        }
