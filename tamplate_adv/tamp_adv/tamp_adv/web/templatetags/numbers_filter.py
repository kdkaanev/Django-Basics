from django import template

register = template.Library()

def only_with_condition(number, condition_func):
    return [x for x in number if condition_func(x)]

@register.filter
def only_odd(number):
   return only_with_condition(number, lambda x: x % 2 > 0)


@register.filter
def only_even(number):
   return [x for x in number if x % 2 == 0]

@register.filter
def only_positive(number):
   return [x for x in number if x > 0]



@register.filter
def only_negative(number):
   return [x for x in number if x < 0]