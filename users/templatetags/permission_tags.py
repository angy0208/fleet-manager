from django import template

from users.permissions import has_permission


register = template.Library()


@register.simple_tag
def user_has_permission(user, module, level):

    return has_permission(
        user,
        module,
        level
    )