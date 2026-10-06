from django.urls import path

from . import views


urlpatterns = [
    path(
        '',
        views.driver_list_view,
        name='driver_list'
    ),
    path(
        'crear/',
        views.driver_create_view,
        name='driver_create'
    ),
    path(
        '<int:driver_id>/',
        views.driver_detail_view,
        name='driver_detail'
    ),
    path(
        '<int:driver_id>/editar/',
        views.driver_edit_view,
        name='driver_edit'
    ),
]