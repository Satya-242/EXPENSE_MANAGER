from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
from django.shortcuts import get_object_or_404
def index(request):
    return render(request, 'index.html')

def add_expense(request):
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add_expense')
    return render(request, 'add_expense.html', {'form': form})

def summary(request):
    expenses = Expense.objects.all()
    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    per_head = round(total / 4, 2)

    contributions = {}
    for name in ['Satya', 'Mani', 'kamal' ]:
        person_total = expenses.filter(paid_by=name).aggregate(Sum('amount'))['amount__sum'] or 0
        contributions[name] = {
            'paid': person_total,
            'balance': round(person_total - per_head, 2)
        }

    return render(request, 'summary.html', {
        'total': total,
        'per_head': per_head,
        'contributions': contributions
    })
    

def all_expenses(request):
    expenses = Expense.objects.all().order_by('-date')
    return render(request, 'all_expenses.html', {'expenses': expenses})

def edit_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    form = ExpenseForm(request.POST or None, instance=expense)
    
    if form.is_valid():
        form.save()
        return redirect('all_expenses')  # redirect to expense list

    return render(request, 'edit_expense.html', {'form': form})


