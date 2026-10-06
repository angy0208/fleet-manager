from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Maintenance
from .forms import MaintenanceForm
from django.contrib import messages
from users.permissions import has_permission

@login_required
def maintenance_list(request):

    if not has_permission(
        request.user,
        'maintenance',
        1
    ):
        messages.error(
            request,
            'No tienes permisos para realizar esta acción.'
        )

        return redirect('dashboard')


    maintenances = Maintenance.objects.all()

    return render(
        request,
        'maintenance/maintenance_list.html',
        {
            'maintenances': maintenances
        }
    )

@login_required
def maintenance_detail(request, pk):

    maintenance = get_object_or_404(
        Maintenance,
        pk=pk
    )

    return render(
        request,
        'maintenance/maintenance_detail.html',
        {
            'maintenance': maintenance
        }
    )


@login_required
def maintenance_create(request):

    if request.method == 'POST':

        form = MaintenanceForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                'maintenance_list'
            )

    else:

        form = MaintenanceForm()

    if not has_permission(
            request.user,
            'maintenance',
            2
    ):
        messages.error(
            request,
            'No tienes permisos para realizar esta acción.'
        )

        return redirect('dashboard')

    return render(
        request,
        'maintenance/maintenance_form.html',
        {
            'form': form,
            'title': 'Registrar mantenimiento'
        }
    )


@login_required
def maintenance_update(request, pk):

    maintenance = get_object_or_404(
        Maintenance,
        pk=pk
    )

    if request.method == 'POST':

        form = MaintenanceForm(
            request.POST,
            instance=maintenance
        )

        if form.is_valid():

            form.save()

            return redirect(
                'maintenance_list'
            )

    else:

        form = MaintenanceForm(
            instance=maintenance
        )

    if not has_permission(
            request.user,
            'maintenance',
            2
    ):
        messages.error(
            request,
            'No tienes permisos para realizar esta acción.'
        )

        return redirect('dashboard')

    return render(
        request,
        'maintenance/maintenance_form.html',
        {
            'form': form,
            'title': 'Editar mantenimiento'
        }
    )