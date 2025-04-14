from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TransactionForm

CATEGORIES = {
    'income': ['Зарплата', 'Фриланс', 'Подарок'],
    'expense': ['Еда', 'Транспорт', 'Развлечения'],
}

@login_required
def base_view(request):
    return render(request, 'finance/base.html')

@login_required
def home(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    balance = sum(t.amount if t.type == 'income' else -t.amount for t in transactions)
    
    return render(request, 'finance/home.html', {
        'transactions': transactions,
        'balance': balance,
        'categories': CATEGORIES,
    })

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('home')
    else:
        form = TransactionForm()
    
    return render(request, 'finance/add_transaction.html', {
        'form': form,
        'categories': CATEGORIES,
    })
from django.shortcuts import get_object_or_404, redirect
from .models import Transaction
from .forms import TransactionForm

@login_required
def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'finance/add_transaction.html', {'form': form})

@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    if request.method == 'POST':
        transaction.delete()
    return redirect('home')
