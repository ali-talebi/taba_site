from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ManagerInformation, DocumentManager
from .forms import ManagerProfileForm, ManagerDocumentsForm , SchoolInformationForm , LevelEducationForm 
from school.models import SchoolInformation , Level_Education_School 
from .models import Province 

@login_required
def manager_dashboard(request):
    provinces = Province.objects.all()
    # دریافت یا ایجاد اطلاعات مدیر
    manager_info, created = ManagerInformation.objects.get_or_create(
        client_manager=request.user
    )
    
    # دریافت یا ایجاد مدارک
    manager_docs, created = DocumentManager.objects.get_or_create(
        manager=manager_info
    )
    
    
    school_info, school_created = SchoolInformation.objects.get_or_create(
        manager=manager_info
    )

    # سطح تحصیلی مدرسه
    level_info, level_created = Level_Education_School.objects.get_or_create(
        school=school_info
    )

    profile_form = ManagerProfileForm(instance=manager_info)
    documents_form = ManagerDocumentsForm(instance=manager_info.documentmanager)
    school_form = SchoolInformationForm(instance=school_info)
    level_form = LevelEducationForm(instance=level_info)
    
    
    if request.method == 'POST':
        if 'save_profile' in request.POST:
            profile_form = ManagerProfileForm(request.POST, instance=manager_info)
            if profile_form.is_valid():
                profile_form.save()

        elif 'save_documents' in request.POST:
            documents_form = ManagerDocumentsForm(request.POST, request.FILES, instance=manager_info.documentmanager)
            if documents_form.is_valid():
                documents_form.save()

        elif 'save_school' in request.POST:
            school_form = SchoolInformationForm(request.POST, request.FILES, instance=school_info)
            if school_form.is_valid():
                school = school_form.save(commit=False)
                school.manager = manager_info
                school.save()

        elif 'save_level' in request.POST:
            level_form = LevelEducationForm(request.POST, instance=level_info)
            if level_form.is_valid():
                level_form.save()

        # ریفرش فرم‌ها بعد از ذخیره
        profile_form = ManagerProfileForm(instance=manager_info)
        documents_form = ManagerDocumentsForm(instance=manager_info.documentmanager)
        school_form = SchoolInformationForm(instance=school_info)
        level_form = LevelEducationForm(instance=level_info)

    return render(request, 'accounts/manager_dashboard.html', {
        'profile_form': profile_form,
        'documents_form': documents_form,
        'school_form': school_form,
        'level_form': level_form,
        'provinces': provinces 
    })