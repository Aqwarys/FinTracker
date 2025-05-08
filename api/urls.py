from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('transactions', views.TransactionViewSet)


app_name = 'api'

urlpatterns = [
    path('transactions/', include(router.urls), name='transactions'),
]
