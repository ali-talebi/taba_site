from django.urls import path
from .views import student_enroll_view , student_enrollment_detail_view



app_name = "academic"
urlpatterns = [
    path('student/enroll/', student_enroll_view, name='student_enroll'),
    path('student/enrollment/', student_enrollment_detail_view, name='student_enrollment_detail'),

]