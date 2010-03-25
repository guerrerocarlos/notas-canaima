from django.template.defaultfilters import stringfilter
from django import template

register = template.Library()


@stringfilter
def trad(value):
    value=value.replace("minutes","minutos")
    value=value.replace("minute","minuto")
    value=value.replace("hour","hora")
    value=value.replace("hours","horas")
    value=value.replace("seconds","segundos")
    return value


register.filter('trad', trad)

