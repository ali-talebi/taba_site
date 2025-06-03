from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ManagerInformation, DocumentManager
from .forms import ManagerProfileForm, ManagerDocumentsForm

@login_required
def manager_dashboard(request):
    # دریافت یا ایجاد اطلاعات مدیر
    manager_info, created = ManagerInformation.objects.get_or_create(
        client_manager=request.user
    )
    
    # دریافت یا ایجاد مدارک
    manager_docs, created = DocumentManager.objects.get_or_create(
        manager=manager_info
    )

    profile_form = ManagerProfileForm(instance=manager_info)
    documents_form = ManagerDocumentsForm(instance=manager_docs)

    if request.method == 'POST':
        if 'save_profile' in request.POST:
            profile_form = ManagerProfileForm(request.POST, instance=manager_info)
            if profile_form.is_valid():
                profile_form.save()

        elif 'save_documents' in request.POST:
            documents_form = ManagerDocumentsForm(request.POST, request.FILES, instance=manager_docs)
            if documents_form.is_valid():
                documents_form.save()

        # ریفرش فرم‌ها بعد از ذخیره
        profile_form = ManagerProfileForm(instance=manager_info)
        documents_form = ManagerDocumentsForm(instance=manager_docs)

    return render(request, 'dashboard/manager_dashboard.html', {
        'profile_form': profile_form,
        'documents_form': documents_form,
    })