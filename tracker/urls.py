from django.urls import path
from . import views
app_name = 'tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>', views.delete_transaction, name='delete_transaction'),
    path('update/<int:pk>', views.update_transaction, name='update_transaction'),
]
