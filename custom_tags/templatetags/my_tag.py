from django import template

register = template.Library()


@register.filter(name='times')
def times(number):
    return range(number)


@register.filter(name='noNone')
def no_none(value):
    if value:
        return value
    else:
        return ''


@register.simple_tag
def filterQuerySet(queryset, start, num):
    return queryset[start: num]


@register.simple_tag
def divide(a, b):
    return int(a / b)
