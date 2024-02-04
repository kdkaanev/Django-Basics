from django import template
from django.contrib.auth.models import User
from django.http import request

register = template.Library()

@register.inclusion_tag('tags/avatar.html', takes_context=True)
def show_avatar(context):
    user = context.request.user
    initials = user.first_name[0] + user.last_name[0] if user.is_authenticated else 'AN'
    return {
        'name': initials,
    }