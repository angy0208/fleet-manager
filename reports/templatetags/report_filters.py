from django import template

register = template.Library()


@register.filter
def spanish_number(value):

    try:
        number = int(value)
    except (TypeError, ValueError):
        return value

    return f"{number:,}".replace(",", ".")

@register.filter
def spanish_currency(value):

    try:
        number = float(value)
    except (TypeError, ValueError):
        return value

    formatted = f"{number:,.2f}"

    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")