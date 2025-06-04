from django import template

register = template.Library()

@register.simple_tag(name='get_file_url')
def get_file_url(obj, field_name):
    field = getattr(obj, field_name, None)
    if field and hasattr(field, 'url'):
        return field.url
    return None

@register.simple_tag(name='get_file_name')
def get_file_name(obj, field_name):
    field = getattr(obj, field_name, None)
    if field and hasattr(field, 'name'):
        return field.name.split('/')[-1]
    return ''