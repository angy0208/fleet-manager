from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Vehicle
from .forms import VehicleForm

from users.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404

@login_required
@permission_required('vehicles', 1)
def vehicle_list_view(request):

    vehicles = Vehicle.objects.all()

    active_vehicles = Vehicle.objects.filter(
        status='active'
    ).count()

    maintenance_vehicles = Vehicle.objects.filter(
        status='maintenance'
    ).count()

    out_service_vehicles = Vehicle.objects.filter(
        status='out_of_service'
    ).count()

    return render(
        request,
        'vehicles/vehicle_list.html',
        {
            'vehicles': vehicles,
            'active_vehicles': active_vehicles,
            'maintenance_vehicles': maintenance_vehicles,
            'out_service_vehicles': out_service_vehicles,
        }
    )


@login_required
@permission_required('vehicles', 2)
def vehicle_create_view(request):

    if request.method == 'POST':

        form = VehicleForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Vehículo registrado correctamente.'
            )

            return redirect('vehicle_list')

    else:

        form = VehicleForm()

    return render(
        request,
        'vehicles/vehicle_form.html',
        {'form': form}
    )

@login_required
@permission_required('vehicles', 1)
def vehicle_detail_view(request, vehicle_id):

    vehicle = get_object_or_404(
        Vehicle,
        id=vehicle_id
    )

    maintenances = vehicle.maintenance_set.all()

    trips = vehicle.trip_set.all()

    last_maintenance = (
        vehicle.maintenance_set
        .filter(status='completed')
        .order_by('-date')
        .first()
    )

    next_maintenance = (
        vehicle.maintenance_set
        .filter(status='scheduled')
        .order_by('date')
        .first()
    )

    return render(
        request,
        'vehicles/vehicle_detail.html',
        {
            'vehicle': vehicle,
            'maintenances': maintenances,
            'trips': trips,
            'last_maintenance': last_maintenance,
            'next_maintenance': next_maintenance
        }
    )

@login_required
@permission_required('vehicles', 2)
def vehicle_edit_view(request, vehicle_id):

    vehicle = get_object_or_404(
        Vehicle,
        id=vehicle_id
    )

    if request.method == 'POST':

        form = VehicleForm(
            request.POST,
            instance=vehicle
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Vehículo actualizado correctamente.'
            )

            return redirect(
                'vehicle_detail',
                vehicle_id=vehicle.id
            )

    else:

        form = VehicleForm(
            instance=vehicle
        )

    return render(
        request,
        'vehicles/vehicle_form.html',
        {
            'form': form,
            'vehicle': vehicle
        }
    )