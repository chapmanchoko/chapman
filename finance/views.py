from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Transaction, Budget, RecurringTransaction, SavingsGoal
from .forms import TransactionForm, BudgetForm, RecurringTransactionForm, SavingsGoalForm
from django.contrib.auth.forms import UserCreationForm

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
    
    # Filtering logic
    transaction_type = request.GET.get('type')
    category = request.GET.get('category')
    date = request.GET.get('date')

    if transaction_type:
        transactions = transactions.filter(type=transaction_type)
    if category:
        transactions = transactions.filter(category__icontains=category)
    if date:
        transactions = transactions.filter(date=date)

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
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'finance/add_transaction.html', {'form': form})

@login_required
def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'finance/edit_transaction.html', {'form': form})

@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'finance/delete_transaction.html', {'transaction': transaction})

# Отображение всех транзакций
@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'finance/transaction_list.html', {'transactions': transactions})

# Отображение всех бюджетов
@login_required
def budget_list(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'finance/budget_list.html', {'budgets': budgets})

@login_required
def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('budget_list')
    else:
        form = BudgetForm()
    return render(request, 'finance/add_budget.html', {'form': form})

@login_required
def edit_budget(request, budget_id):
    budget = get_object_or_404(Budget, id=budget_id, user=request.user)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('budget_list')
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'finance/edit_budget.html', {'form': form})

@login_required
def delete_budget(request, budget_id):
    budget = get_object_or_404(Budget, id=budget_id, user=request.user)
    if request.method == 'POST':
        budget.delete()
        return redirect('budget_list')
    return render(request, 'finance/delete_budget.html', {'budget': budget})

# Отображение всех повторяющихся транзакций
@login_required
def recurring_transaction_list(request):
    recurring_transactions = RecurringTransaction.objects.filter(user=request.user)
    return render(request, 'finance/recurring_transaction_list.html', {'recurring_transactions': recurring_transactions})

@login_required
def add_recurring_transaction(request):
    if request.method == 'POST':
        form = RecurringTransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('recurring_transaction_list')
    else:
        form = RecurringTransactionForm()
    return render(request, 'finance/add_recurring_transaction.html', {'form': form})

@login_required
def edit_recurring_transaction(request, transaction_id):
    transaction = get_object_or_404(RecurringTransaction, id=transaction_id, user=request.user)
    if request.method == 'POST':
        form = RecurringTransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('recurring_transaction_list')
    else:
        form = RecurringTransactionForm(instance=transaction)
    return render(request, 'finance/edit_recurring_transaction.html', {'form': form})

@login_required
def delete_recurring_transaction(request, transaction_id):
    transaction = get_object_or_404(RecurringTransaction, id=transaction_id, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('recurring_transaction_list')
    return render(request, 'finance/delete_recurring_transaction.html', {'transaction': transaction})

# Отображение целей сбережений
@login_required
def savings_goal_list(request):
    savings_goals = SavingsGoal.objects.filter(user=request.user)
    return render(request, 'finance/savings_goal_list.html', {'savings_goals': savings_goals})

@login_required
def add_savings_goal(request):
    if request.method == 'POST':
        form = SavingsGoalForm(request.POST, request.FILES)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('savings_goal_list')
    else:
        form = SavingsGoalForm()
    return render(request, 'finance/add_savings_goal.html', {'form': form})

@login_required
def edit_savings_goal(request, goal_id):
    goal = get_object_or_404(SavingsGoal, id=goal_id, user=request.user)
    if request.method == 'POST':
        form = SavingsGoalForm(request.POST, request.FILES, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('savings_goal_list')
    else:
        form = SavingsGoalForm(instance=goal)
    return render(request, 'finance/edit_savings_goal.html', {'form': form})

@login_required
def delete_savings_goal(request, goal_id):
    goal = get_object_or_404(SavingsGoal, id=goal_id, user=request.user)
    if request.method == 'POST':
        goal.delete()
        return redirect('savings_goal_list')
    return render(request, 'finance/delete_savings_goal.html', {'goal': goal})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу входа после успешной регистрации
    else:
        form = UserCreationForm()
    return render(request, 'finance/register.html', {'form': form})
