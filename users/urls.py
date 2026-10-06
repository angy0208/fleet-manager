from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('vehicle-test/', views.vehicle_test_view, name='vehicle_test'),
    path('vehicle-list-test/', views.vehicle_list_test_view, name='vehicle_list_test'),
]
