from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Driver
from .forms import DriverForm

from users.decorators import permission_required


@login_required
@permission_required('drivers', 1)
def driver_list_view(request):

    drivers = Driver.objects.all()

    return render(
        request,
        'drivers/driver_list.html',
        {'drivers': drivers}
    )


@login_required
@permission_required('drivers', 2)
def driver_create_view(request):

    if request.method == 'POST':

        form = DriverForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Conductor registrado correctamente.'
            )

            return redirect('driver_list')

    else:

        form = DriverForm()

    return render(
        request,
        'drivers/driver_form.html',
        {'form': form}
    )


@login_required
@permission_required('drivers', 1)
def driver_detail_view(request, driver_id):

    driver = get_object_or_404(
        Driver,
        id=driver_id
    )

    return render(
        request,
        'drivers/driver_detail.html',
        {'driver': driver}
    )


@login_required
@permission_required('drivers', 2)
def driver_edit_view(request, driver_id):

    driver = get_object_or_404(
        Driver,
        id=driver_id
    )

    if request.method == 'POST':

        form = DriverForm(
            request.POST,
            instance=driver
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Conductor actualizado correctamente.'
            )

            return redirect(
                'driver_detail',
                driver_id=driver.id
            )

    else:

        form = DriverForm(
            instance=driver
        )

    return render(
        request,
        'drivers/driver_form.html',
        {
            'form': form,
            'driver': driver
        }
    )