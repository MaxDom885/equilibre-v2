from django import template

register = template.Library()

@register.filter(name='batch')
def batch(value, arg):
    """
    Divide a list into sublists of size `arg`.
    """
    try:
        size = int(arg)
    except ValueError:
        return value  # Return the original list if the argument is not an integer

    return [value[i:i + size] for i in range(0, len(value), size)]
