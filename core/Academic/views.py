# enrollments/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EnrollmentForm
from student.models import StudentInformation
from .models import Enrollment
from school.models import Level_Education_School , Field_Education_School 


def student_enroll_view(request):
    student = StudentInformation.objects.get(client_student=request.user)
    enrollment_qs = Enrollment.objects.filter(student=student)
    
    
    enrollment = Enrollment.objects.filter(student=student).last()

    if enrollment and enrollment.approved:
        # اگر تایید شده بود، به جای فرم ثبت‌نام صفحه جزئیات رو نشون بده
        return redirect('academic:student_enrollment_detail')
    

    enrollment = enrollment_qs.first()  # فرض می‌کنیم هر دانش آموز فقط یک ثبت نام داره
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.student = student
            enrollment.save()
            return redirect('academic:student_enrollment_detail')
    else:
        form = EnrollmentForm(instance=enrollment)

    levels = Level_Education_School.objects.all()
    fields = Field_Education_School.objects.all()

    context = {
        'form': form,
        'levels': levels,
        'fields': fields,
    }
    return render(request, 'student/student_enrollment_form.html', context)


@login_required
def student_enrollment_detail_view(request):
    student = StudentInformation.objects.get(client_student=request.user)
    enrollment = Enrollment.objects.filter(student=student).first()  # حتما کوئری درست بزن


    return render(request, 'student/student_enrollment_detail.html', {
        'enrollment': enrollment
    })