from django.shortcuts import render, redirect
from .forms import ManagerRegistrationForm, StudentRegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from school.models import SchoolInformation
from manager.models import ManagerInformation 



# Common logout view
def logout_view(request):
    logout(request)
    return redirect('accounts:login')  # or student login depending on user type

def home_view(request):
    manager_form = ManagerRegistrationForm()
    student_form = StudentRegistrationForm()
    return render(request, 'accounts/home.html', {
        'manager_form': manager_form,
        'student_form': student_form
    })
    
def manager_register(request):
    
    if request.user.is_authenticated :
        if request.user.user_type == 'manager': 
            return redirect('accounts:manager_dashboard')
        else : 
            return redirect('accounts:student_dashboard')
    
    if request.method == 'POST':
        form = ManagerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # اختیاری: بعد از ثبت نام وارد شود
            return redirect('accounts:login')  # جایگزین کن با اسم url مناسب
    else:
        form = ManagerRegistrationForm()
    
    return render(request, 'accounts/manager_register.html', {'form': form})

def student_register(request):
    
    if request.user.is_authenticated :
        if request.user.user_type == 'manager': 
            return redirect('accounts:manager_dashboard')
        else : 
            return redirect('accounts:student_dashboard')
    
    
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'accounts/student_register.html', {'form': form})

# Manager Login View
def manager_login(request):
    
    if request.user.is_authenticated :
        if request.user.user_type == 'manager': 
            return redirect('accounts:manager_dashboard')
        else : 
            return redirect('accounts:student_dashboard')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None and user.user_type == 'manager':
            login(request, user)
            return redirect('manager:manager_dashboard')
        else:
            error = "Invalid credentials or not a manager"
            return render(request, 'accounts/manager_login.html', {'error': error})
    return render(request, 'accounts/manager_login.html')

# Student Login View
def student_login(request):
    
    if request.user.is_authenticated :
        if request.user.user_type == 'manager': 
            return redirect('accounts:manager_dashboard')
        else : 
            return redirect('accounts:student_dashboard')
        
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None and user.user_type == 'student':
            login(request, user)
            return redirect('accounts:student_dashboard')
        else:
            error = "Invalid credentials or not a student"
            return render(request, 'accounts/student_login.html', {'error': error})
    return render(request, 'accounts/student_login.html')

# Manager Dashboard
@login_required
def manager_dashboard(request):
    
    
    if request.user.user_type != 'manager':
        return redirect('student_dashboard')
    
    # total_school = ManagerInformation.objects.filter(manager = request.user )
    
    return render(request, 'manager/manager_dashboard.html' , {'data':None})

# Student Dashboard
@login_required
def student_dashboard(request):
    if request.user.user_type != 'student':
        return redirect('accounts:manager_dashboard')
    return render(request, 'accounts/student_login.html' , {})
