from django.urls import path

from . import views


urlpatterns = [
    path('', views.vehicle_list_view, name='vehicle_list'),
    path('crear/', views.vehicle_create_view, name='vehicle_create'),
    path('<int:vehicle_id>/', views.vehicle_detail_view, name='vehicle_detail'),
    path('<int:vehicle_id>/editar/', views.vehicle_edit_view, name='vehicle_edit'),

]