from django import forms
from .models import Transaction, Budget, RecurringTransaction, SavingsGoal

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['type', 'category', 'amount', 'date', 'description']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'limit', 'start_date', 'end_date']

class RecurringTransactionForm(forms.ModelForm):
    class Meta:
        model = RecurringTransaction
        fields = ['type', 'category', 'amount', 'frequency', 'next_date']

class SavingsGoalForm(forms.ModelForm):
    class Meta:
        model = SavingsGoal
        fields = ['name', 'target_amount', 'current_amount', 'deadline']
