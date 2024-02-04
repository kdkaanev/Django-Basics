from django import template
from django.template.defaultfilters import safe
from django.utils import timezone

register = template.Library()


@register.simple_tag
def list_of(values):
    item_string = [f'<li>{value}</li>' for value in values]
    return safe(f'<ul>{"".join(item_string)}</ul>')

@register.simple_tag
def current_datetime(format_string):

    return timezone.now().strftime(format_string)