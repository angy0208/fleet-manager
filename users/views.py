from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import LoginForm
from .decorators import permission_required

def login_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        form = LoginForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('dashboard')

    else:

        form = LoginForm()

    return render(
        request,
        'users/login.html',
        {'form': form}
    )


@login_required
def logout_view(request):

    logout(request)

    messages.success(
        request,
        'Sesión cerrada correctamente'
    )

    return redirect('login')

@login_required
def dashboard_view(request):

    return render(
        request,
        'users/dashboard.html'
    )

@login_required
@permission_required('vehicles', 2)
def vehicle_test_view(request):

    return render(
        request,
        'users/vehicle_test.html'
    )

@login_required
@permission_required('vehicles', 1)
def vehicle_list_test_view(request):

    return render(
        request,
        'users/vehicle_list_test.html'
    )