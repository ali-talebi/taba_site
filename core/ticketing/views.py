from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import TicketInformation
from manager.models import ManagerInformation 
from student.models import StudentInformation

@login_required
def send_ticket_view(request):
    form = TicketForm()

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.client_ticket = request.user

            if ManagerInformation.objects.filter(client_manager=request.user).exists():
                ticket.user_type = 'manager'
            else:
                ticket.user_type = 'student'

            ticket.save()
            return redirect('ticket:ticket_list')  # مقصد رو بسته به url خودت تنظیم کن

    return render(request, 'ticket/send_ticket.html', {'form': form})



@login_required
def ticket_list_view(request):
    user_tickets = TicketInformation.objects.filter(client_ticket=request.user).order_by('-id')
    return render(request, 'ticket/ticket_list.html', {'tickets': user_tickets})