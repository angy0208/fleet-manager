from django.urls import path

from . import views


urlpatterns = [
    path('', views.trip_list_view, name='trip_list'),
    path('crear/', views.trip_create_view, name='trip_create'),
    path('<int:trip_id>/', views.trip_detail_view, name='trip_detail'),
    path('<int:trip_id>/editar/', views.trip_edit_view, name='trip_edit'),
]