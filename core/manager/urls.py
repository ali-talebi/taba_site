from django.urls import path
from .views import (
    manager_dashboard_menu,
    profile_form_view,
    school_info_form_view,
    # school_level_form_view,
    documents_form_view,
)


app_name = "manager"
urlpatterns = [
    path('dashboard/', manager_dashboard_menu, name='manager_dashboard'),
    path('profile/', profile_form_view, name='profile_form'),
    path('school/info/', school_info_form_view, name='school_info_form'),
    # path('manager/school/level/', school_level_form_view, name='school_level_form'),
    path('manager/documents/', documents_form_view, name='documents_form'),
]