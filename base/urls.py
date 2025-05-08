from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls', namespace='tracker')),
    path('export_data/', include('export_data.urls', namespace='export_data')),
    path('api/', include('api.urls', namespace='api')),
]
