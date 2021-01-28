import uuid as uuidlib

from django import template

register = template.Library()

@register.simple_tag
def uuid():
    return str(uuidlib.uuid4())
