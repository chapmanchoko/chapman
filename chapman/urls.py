"""
URL configuration for chapman project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from finance import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base_view, name='base'),
    path('home/', views.home, name='home'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('', auth_views.LoginView.as_view(template_name='finance/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('edit/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
    path('delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
]