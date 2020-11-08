from django import template

register = template.Library()

@register.simple_tag
def store_title() -> str:
    return "PiLib"