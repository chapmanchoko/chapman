from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('recurring-transactions/', views.recurring_transaction_list, name='recurring_transaction_list'),
    path('recurring-transactions/add/', views.add_recurring_transaction, name='add_recurring_transaction'),
    path('recurring-transactions/edit/<int:transaction_id>/', views.edit_recurring_transaction, name='edit_recurring_transaction'),
    path('recurring-transactions/delete/<int:transaction_id>/', views.delete_recurring_transaction, name='delete_recurring_transaction'),
    path('budgets/add/', views.add_budget, name='add_budget'),
    path('budgets/edit/<int:budget_id>/', views.edit_budget, name='edit_budget'),
    path('budgets/delete/<int:budget_id>/', views.delete_budget, name='delete_budget'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/add/', views.add_transaction, name='add_transaction'),
    path('transactions/edit/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
    path('transactions/delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path('budgets/', views.budget_list, name='budget_list'),
    path('recurring-transactions/', views.recurring_transaction_list, name='recurring_transaction_list'),
    path('savings-goals/', views.savings_goal_list, name='savings_goal_list'),
    path('edit/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
    path('delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path('savings-goals/add/', views.add_savings_goal, name='add_savings_goal'),
    path('savings-goals/edit/<int:goal_id>/', views.edit_savings_goal, name='edit_savings_goal'),
    path('savings-goals/delete/<int:goal_id>/', views.delete_savings_goal, name='delete_savings_goal'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)