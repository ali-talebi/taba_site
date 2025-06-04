from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import StudentInformation, Province
from .forms import StudentProfileForm
from .models import StudentInformation, Document_Authenticate_Student
from .forms import StudentAuthenticationDocumentForm
from .models import StudentInformation, Document_Education_Student
from .forms import StudentEducationDocumentForm

@login_required
def student_dashboard_menu(request):
    return render(request, 'student/student_dashboard_menu.html')

@login_required
def student_profile_form_view(request):
    # دریافت یا ایجاد اطلاعات دانش آموز
    student_info, created = StudentInformation.objects.get_or_create(
        client_student=request.user
    )

    profile_form = StudentProfileForm(instance=student_info)
    provinces = Province.objects.all()

    if request.method == 'POST':
        profile_form = StudentProfileForm(request.POST, instance=student_info)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('student_dashboard')

    return render(request, 'student/student_profile_form.html', {
        'profile_form': profile_form,
        'provinces': provinces
    })
    


@login_required
def student_authentication_form_view(request):
    # دریافت یا ایجاد اطلاعات دانش آموز
    student_info, created = StudentInformation.objects.get_or_create(
        client_student=request.user
    )

    # دریافت یا ایجاد مدارک هویتی
    try:
        auth_docs = student_info.document_authenticate_student
    except Document_Authenticate_Student.DoesNotExist:
        auth_docs = Document_Authenticate_Student(student=student_info)

    auth_form = StudentAuthenticationDocumentForm(instance=auth_docs)

    if request.method == 'POST':
        auth_form = StudentAuthenticationDocumentForm(request.POST, request.FILES, instance=auth_docs)
        if auth_form.is_valid():
            auth_form.save()
            return redirect('student:student_dashboard')

    return render(request, 'student/student_authentication_form.html', {
        'auth_form': auth_form,
        'auth_docs': auth_docs
    })
    
    
@login_required
def student_education_form_view(request):
    student_info, created = StudentInformation.objects.get_or_create(
        client_student=request.user
    )

    try:
        edu_docs = student_info.document_education_student
    except Document_Education_Student.DoesNotExist:
        edu_docs = Document_Education_Student(student=student_info)

    edu_form = StudentEducationDocumentForm(instance=edu_docs)

    if request.method == 'POST':
        edu_form = StudentEducationDocumentForm(request.POST, request.FILES, instance=edu_docs)
        if edu_form.is_valid():
            edu_form.save()
            return redirect('student:student_dashboard')

    # جداگانه فایل‌ها رو به قالب میدیم
    files = {
        'file1': getattr(edu_docs, 'file1', None),
        'file2': getattr(edu_docs, 'file2', None),
        'file3': getattr(edu_docs, 'file3', None),
        'file4': getattr(edu_docs, 'file4', None),
        'file5': getattr(edu_docs, 'file5', None),
        'file6': getattr(edu_docs, 'file6', None),
        'file7': getattr(edu_docs, 'file7', None),
        'file8': getattr(edu_docs, 'file8', None),
        'file9': getattr(edu_docs, 'file9', None),
        'file10': getattr(edu_docs, 'file10', None),
        'file11': getattr(edu_docs, 'file11', None),
        'file12': getattr(edu_docs, 'file12', None),
    }

    return render(request, 'student/student_education_form.html', {
        'edu_form': edu_form,
        'edu_docs': edu_docs,
        'files': files
    })