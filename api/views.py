from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from tracker.models import Transaction
from .serializer import TransactionSerializer

class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
