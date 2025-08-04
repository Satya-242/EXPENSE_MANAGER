from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add_expense, name='add_expense'),
    path('summary/', views.summary, name='summary'),
    path('expenses/', views.all_expenses, name='all_expenses'),
    path('edit/<int:expense_id>/', views.edit_expense, name='edit_expense'),  # ← Comma added here
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]
