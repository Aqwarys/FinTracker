from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    operation_choices = [
        ('Income', 'Income'),
        ('Expense', 'Expense')
    ]
    operation_type = models.CharField(max_length=10, choices=operation_choices)
    amount  = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.operation_type

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Transactions'
        verbose_name = 'Transaction'
