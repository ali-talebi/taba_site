from django.urls import path 
from . import views

app_name = "accounts"
urlpatterns = [
    path('' , views.home_view , name="login" ) , 
    path('logout/' , views.logout_view , name="logout" ) , 
    path('manager/register/', views.manager_register, name='manager_register'),
    path('student/register/', views.student_register, name='student_register'),
    path('manager/login/', views.manager_login, name='manager_login'),
    path('student/login/', views.student_login, name='student_login'),
    
]

