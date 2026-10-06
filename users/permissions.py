from .models import Role,UserRole

PERMISSION_MODULES = [
    'vehicles',
    'drivers',
    'trips',
    'maintenance',
    'expenses',
    'reports',
]

def get_user_role(user):
    user_role = UserRole.objects.filter(
        user=user
    ).first()

    if user_role:
        return user_role.role

    return None

def has_permission(user, module, required_level):

    if module not in PERMISSION_MODULES:
        raise ValueError(
            f"Invalid permission module: {module}"
        )

    role = get_user_role(user)

    if not role:
        return False

    permission_level = getattr(
        role,
        module
    )

    return permission_level >= required_level