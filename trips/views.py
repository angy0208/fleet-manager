from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Trip
from .forms import TripForm

from users.decorators import permission_required

@login_required
@permission_required('trips', 1)
def trip_list_view(request):
    trips = Trip.objects.all()
    return render(
        request,
        'trips/trip_list.html',
        {'trips': trips}
    )

@login_required
@permission_required('trips', 2)
def trip_create_view(request):
    if request.method == 'POST':
        form = TripForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Viaje registardo correctamente.'
            )
            return redirect('trip_list')
    else:
        form = TripForm()
    return render(
        request,
    'trips/trip_form.html',
        {'form': form}
    )

@login_required
@permission_required('trips', 2)
def trip_detail_view(request, trip_id):

    trip = get_object_or_404(
        Trip,
        id=trip_id
    )

    return render(
        request,
        'trips/trip_detail.html',
        {'trip': trip}
    )

@login_required
@permission_required('trips', 2)
def trip_edit_view(request, trip_id):

    trip = get_object_or_404(
        Trip,
        id=trip_id
    )

    if request.method == 'POST':

        form = TripForm(
            request.POST,
            instance=trip
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Viaje actualizado correctamente.'
            )

            return redirect(
                'trip_detail',
                trip_id=trip.id
            )

    else:

        form = TripForm(
            instance=trip
        )

    return render(
        request,
        'trips/trip_form.html',
        {
            'form': form,
            'trip': trip
        }
    )