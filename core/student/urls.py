from django.urls import path
from .views import (
    student_dashboard_menu,
    student_profile_form_view,
    student_authentication_form_view,
    student_education_form_view
)

app_name = "student"
urlpatterns = [
    path('dashboard/', student_dashboard_menu, name='student_dashboard'),
    path('profile/', student_profile_form_view, name='student_profile_form'),
    path('authentication/', student_authentication_form_view, name='student_authentication_form'),
    path('education/', student_education_form_view, name='student_education_form'),
]