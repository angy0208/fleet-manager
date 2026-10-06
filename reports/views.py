from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from vehicles.models import Vehicle
from drivers.models import Driver
from trips.models import Trip
from maintenance.models import Maintenance
from expenses.models import Expense

from django.db.models import Sum, Avg, Max
from django.utils import timezone
from datetime import timedelta

@login_required
def dashboard_view(request):
    total_expense_amount = Expense.objects.aggregate(
        total=Sum('amount')
    )['total'] or 0

    total_maintenance_cost = Maintenance.objects.aggregate(
        total=Sum('cost')
    )['total'] or 0

    average_mileage = Vehicle.objects.aggregate(
        average=Avg('current_mileage')
    )['average'] or 0

    highest_mileage = Vehicle.objects.aggregate(
        maximum=Max('current_mileage')
    )['maximum'] or 0

    fuel_expenses = Expense.objects.filter(
        expense_type='fuel'
    ).aggregate(
        total=Sum('amount')
    )['total'] or 0

    toll_expenses = Expense.objects.filter(
        expense_type='toll'
    ).aggregate(
        total=Sum('amount')
    )['total'] or 0

    allowance_expenses = Expense.objects.filter(
        expense_type='allowance'
    ).aggregate(
        total=Sum('amount')
    )['total'] or 0

    washing_expenses = Expense.objects.filter(
        expense_type='washing'
    ).aggregate(
        total=Sum('amount')
    )['total'] or 0

    insurance_expenses = Expense.objects.filter(
        expense_type='insurance'
    ).aggregate(
        total=Sum('amount')
    )['total'] or 0

    other_expenses = Expense.objects.filter(
        expense_type='other'
    ).aggregate(
        total=Sum('amount')
    )['total'] or 0

    today = timezone.now().date()

    current_month_expenses = Expense.objects.filter(
        date__year=today.year,
        date__month=today.month
    ).aggregate(
        total=Sum('amount')
    )['total'] or 0

    current_month_maintenance = Maintenance.objects.filter(
        date__year=today.year,
        date__month=today.month
    ).aggregate(
        total=Sum('cost')
    )['total'] or 0

    current_month_total = (
        current_month_expenses +
        current_month_maintenance
    )

    preventive_maintenance = Maintenance.objects.filter(
        category='preventive'
    ).aggregate(
        total=Sum('cost')
    )['total'] or 0

    corrective_maintenance = Maintenance.objects.filter(
        category='corrective'
    ).aggregate(
        total=Sum('cost')
    )['total'] or 0

    vehicle_monthly_costs = []

    today = timezone.now().date()

    for vehicle in Vehicle.objects.all():

        vehicle_expenses = Expense.objects.filter(
            vehicle=vehicle,
            date__year=today.year,
            date__month=today.month
        ).aggregate(
            total=Sum('amount')
        )['total'] or 0

        vehicle_maintenance = Maintenance.objects.filter(
            vehicle=vehicle,
            date__year=today.year,
            date__month=today.month
        ).aggregate(
            total=Sum('cost')
        )['total'] or 0

        vehicle_total = (
            vehicle_expenses +
            vehicle_maintenance
        )

        vehicle_monthly_costs.append({
            'vehicle': vehicle,
            'expenses': vehicle_expenses,
            'maintenance': vehicle_maintenance,
            'total': vehicle_total,
        })

    today = timezone.now().date()

    license_alert_date = today + timedelta(days=30)

    expired_licenses = Driver.objects.filter(
        license_expiry__lt=today,
        status='active'
    )

    expiring_licenses = Driver.objects.filter(
        license_expiry__gte=today,
        license_expiry__lte=license_alert_date,
        status='active'
    )

    vehicles_in_maintenance = Vehicle.objects.filter(
        status='maintenance'
    )

    scheduled_maintenance = Maintenance.objects.filter(
        status='scheduled',
        date__gte=today
    ).order_by('date')

    context = {

        'total_expense_amount': total_expense_amount,

        'total_maintenance_cost': total_maintenance_cost,

        'average_mileage': round(
            average_mileage
        ),

        'highest_mileage': highest_mileage,

        'total_vehicles': Vehicle.objects.count(),

        'active_vehicles': Vehicle.objects.filter(
            status='active'
        ).count(),

        'maintenance_vehicles': Vehicle.objects.filter(
            status='maintenance'
        ).count(),

        'out_service_vehicles': Vehicle.objects.filter(
            status='out_of_service'
        ).count(),


        'total_drivers': Driver.objects.count(),

        'active_drivers': Driver.objects.filter(
            status='active'
        ).count(),


        'total_trips': Trip.objects.count(),

        'completed_trips': Trip.objects.filter(
            status='completed'
        ).count(),

        'scheduled_trips': Trip.objects.filter(
            status='scheduled'
        ).count(),


        'total_maintenance': Maintenance.objects.count(),

        'total_expenses': Expense.objects.count(),

        'fuel_expenses': fuel_expenses,

        'toll_expenses': toll_expenses,

        'allowance_expenses': allowance_expenses,

        'washing_expenses': washing_expenses,

        'insurance_expenses': insurance_expenses,

        'other_expenses': other_expenses,

        'current_month_expenses': current_month_expenses,

        'current_month_maintenance': current_month_maintenance,

        'current_month_total': current_month_total,

        'vehicle_monthly_costs': vehicle_monthly_costs,

        'preventive_maintenance': preventive_maintenance,

        'corrective_maintenance': corrective_maintenance,

        'expired_licenses': expired_licenses,

        'expiring_licenses': expiring_licenses,

        'vehicles_in_maintenance': vehicles_in_maintenance,

        'scheduled_maintenance': scheduled_maintenance,
    }


    return render(
        request,
        'reports/dashboard.html',
        context
    )