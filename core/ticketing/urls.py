from django.urls import path
from . import views

app_name = 'ticket'

urlpatterns = [
    path('send/', views.send_ticket_view, name='send_ticket'),
    path('list/', views.ticket_list_view, name='ticket_list'),
]