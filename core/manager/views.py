from django.shortcuts import render, get_object_or_404 , redirect 
from django.contrib.auth.decorators import login_required
from .models import ManagerInformation, DocumentManager
from .forms import ManagerProfileForm, ManagerDocumentsForm , SchoolInformationForm , LevelEducationForm 
from school.models import SchoolInformation , Level_Education_School 
from .models import Province 


@login_required
def manager_dashboard_menu(request):
    return render(request, 'manager/manager_dashboard_menu.html')

@login_required
def profile_form_view(request):
    manager_info, created = ManagerInformation.objects.get_or_create(
        client_manager=request.user
    )

    profile_form = ManagerProfileForm(instance=manager_info)

    if request.method == 'POST':
        profile_form = ManagerProfileForm(request.POST, instance=manager_info)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('manager:manager_dashboard')

    provinces = Province.objects.all()

    return render(request, 'manager/profile_form_manager.html', {
        'profile_form': profile_form,
        'provinces': provinces
    })
    
    
    
@login_required
def school_info_form_view(request):
    manager_info, created = ManagerInformation.objects.get_or_create(client_manager=request.user)
    school_info, _ = SchoolInformation.objects.get_or_create(manager=manager_info)
    school_form = SchoolInformationForm(instance=school_info)

    if school_info.status == 'approved' : 
        return redirect('manager:school_status_view')
    if request.method == 'POST':
        school_form = SchoolInformationForm(request.POST, request.FILES, instance=school_info)
        if school_form.is_valid():
            school_form.save()
            return redirect('manager:school_status_view')

    provinces = Province.objects.all()

    return render(request, 'manager/school_info_form.html', {
        'school_form': school_form,
        'provinces': provinces
    })
    
    

@login_required
def school_status_view(request):
    manager_info = ManagerInformation.objects.get(client_manager=request.user)
    school_info = SchoolInformation.objects.filter(manager=manager_info).first()

    return render(request, 'manager/school_status.html', {
        'school_info': school_info
    })    


@login_required
def documents_form_view(request):
    # دریافت یا ایجاد اطلاعات مدیر
    manager_info, created = ManagerInformation.objects.get_or_create(
        client_manager=request.user
    )

    # دریافت یا ایجاد مدارک
    try:
        document_instance = manager_info.documentmanager
    except DocumentManager.DoesNotExist:
        document_instance = DocumentManager(manager=manager_info)

    documents_form = ManagerDocumentsForm(instance=document_instance)

    if request.method == 'POST':
        documents_form = ManagerDocumentsForm(request.POST, request.FILES, instance=document_instance)
        if documents_form.is_valid():
            documents_form.save()
            return redirect('manager:manager_dashboard')  # بازگشت به منوی اصلی

    return render(request, 'manager/document_manager_form.html', {
        'documents_form': documents_form,
        'document_instance': document_instance,  # مهم: برای نمایش وضعیت فعلی فایل‌ها
    })