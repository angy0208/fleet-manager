from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Expense
from .forms import ExpenseForm

from users.decorators import permission_required


@login_required
@permission_required('expenses', 1)
def expense_list_view(request):

    expenses = Expense.objects.all()

    return render(
        request,
        'expenses/expense_list.html',
        {
            'expenses': expenses
        }
    )


@login_required
@permission_required('expenses', 2)
def expense_create_view(request):

    if request.method == 'POST':

        form = ExpenseForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Gasto registrado correctamente.'
            )

            return redirect(
                'expense_list'
            )

    else:

        form = ExpenseForm()


    return render(
        request,
        'expenses/expense_form.html',
        {
            'form': form
        }
    )
@login_required
@permission_required('expenses', 1)
def expense_detail_view(request, expense_id):

    expense = get_object_or_404(
        Expense,
        id=expense_id
    )

    return render(
        request,
        'expenses/expense_detail.html',
        {
            'expense': expense
        }
    )

@login_required
@permission_required('expenses', 2)
def expense_edit_view(request, expense_id):

    expense = get_object_or_404(
        Expense,
        id=expense_id
    )


    if request.method == 'POST':

        form = ExpenseForm(
            request.POST,
            instance=expense
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Gasto actualizado correctamente.'
            )

            return redirect(
                'expense_detail',
                expense_id=expense.id
            )


    else:

        form = ExpenseForm(
            instance=expense
        )


    return render(
        request,
        'expenses/expense_form.html',
        {
            'form': form,
            'expense': expense
        }
    )