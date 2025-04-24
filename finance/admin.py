# filepath: c:\Users\admin\Documents\projects\chapman\finance\admin.py
from django.contrib import admin
from .models import Transaction, Budget, RecurringTransaction, SavingsGoal

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'type', 'category', 'amount', 'date']  # Убедитесь, что 'user' есть в модели
    list_filter = ('type', 'date')
    search_fields = ('category', 'description')

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'limit', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('category',)

@admin.register(RecurringTransaction)
class RecurringTransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'category', 'amount', 'frequency', 'next_date')
    list_filter = ('frequency', 'next_date')
    search_fields = ('category',)

@admin.register(SavingsGoal)
class SavingsGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'target_amount', 'current_amount', 'deadline')
    list_filter = ('deadline',)
    search_fields = ('name',)
