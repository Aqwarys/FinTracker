from django.urls import path
from . import views

app_name = 'export_data'

urlpatterns = [
    path('', views.export_data, name='export_data'),
]
