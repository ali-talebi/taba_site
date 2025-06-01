from django.urls import path 
from . import views

app_name = "accounts"
urlpatterns = [
    path('home/' , views.home_view , name="login" ) , 
    path('logout/' , views.logout_view , name="logout" ) , 
    path('manager/register/', views.manager_register, name='manager_register'),
    path('student/register/', views.student_register, name='student_register'),
    path('manager/login/', views.manager_login, name='manager_login'),
    path('student/login/', views.student_login, name='student_login'),
    path('manager/dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    
]

