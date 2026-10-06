from django.urls import path

from . import views

urlpatterns = [
    path('', views.expense_list_view, name='expense_list'),
    path('create/', views.expense_create_view, name='expense_create'),
    path('<int:expense_id>/', views.expense_detail_view, name='expense_detail'),
    path('<int:expense_id>/edit/', views.expense_edit_view, name='expense_edit'),
]
