from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

from .permissions import has_permission


def permission_required(module, level):

    def decorator(view_func):

        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            if has_permission(
                request.user,
                module,
                level
            ):
                return view_func(
                    request,
                    *args,
                    **kwargs
                )

            messages.error(
                request,
                'No tiene permisos para realizar esta acción.'
            )

            return redirect('dashboard')

        return wrapper

    return decorator