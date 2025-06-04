from django.urls import path
from .views import manager_dashboard


app_name = "manager"
urlpatterns = [
    path('dashboard/', manager_dashboard, name='manager_dashboard'),
]